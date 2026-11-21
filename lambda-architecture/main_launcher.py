import tkinter as tk
from tkinter import scrolledtext, messagebox, font
import subprocess
import threading
import sys
import os
import queue
import webbrowser
import socket
import time

class LambdaCommandCenter:
    def __init__(self, root):
        self.root = root
        self.root.title("Medical IoT - Lambda Architecture Command Center (Educational)")
        self.root.geometry("1500x900")
        self.root.configure(bg="#0b0f19") # Deep dark theme

        self.msg_queue = queue.Queue()
        self.processes = {}
        
        # Global stats counters
        self.counters = {
            "SENSOR": tk.IntVar(value=0),
            "ANOMALIES": tk.IntVar(value=0)
        }

        # Infrastructure states (Kafka, Postgres, MLflow, FastAPI)
        self.infra_status = {
            "Kafka (9092)": False,
            "Postgres (5432)": False,
            "MLflow (5001)": False,
            "FastAPI API (8000)": False
        }

        self.setup_styles()
        self.create_layout()
        self.update_loop()
        
        # Start background health monitoring thread
        self.infra_running = True
        self.infra_thread = threading.Thread(target=self.monitor_infrastructure, daemon=True)
        self.infra_thread.start()

    def setup_styles(self):
        """Defines modern developer terminal color scheme and fonts"""
        self.colors = {
            "bg": "#0b0f19",
            "panel": "#1e293b",
            "text": "#e2e8f0",
            "header": "#0f172a",
            "accent": "#38bdf8",
            "success": "#10b981",
            "warning": "#f59e0b",
            "danger": "#ef4444",
            "batch": "#a855f7",
            "serving": "#ec4899",
            "gray": "#475569"
        }
        self.fonts = {
            "title": font.Font(family="Consolas", size=16, weight="bold"),
            "subtitle": font.Font(family="Segoe UI", size=10, weight="bold"),
            "desc": font.Font(family="Segoe UI", size=8, slant="italic"),
            "console": font.Font(family="Consolas", size=8),
            "btn": font.Font(family="Segoe UI", size=8, weight="bold")
        }

    def check_port(self, host, port):
        try:
            with socket.create_connection((host, port), timeout=0.3):
                return True
        except:
            return False

    def monitor_infrastructure(self):
        """Periodically checks ports for required services in the background"""
        while self.infra_running:
            self.infra_status["Kafka (9092)"] = self.check_port("localhost", 9092)
            self.infra_status["Postgres (5432)"] = self.check_port("localhost", 5432)
            self.infra_status["MLflow (5001)"] = self.check_port("localhost", 5001)
            self.infra_status["FastAPI API (8000)"] = self.check_port("localhost", 8000)
            
            # Request GUI update
            self.msg_queue.put(("INFRA_UPDATE", None, None))
            time.sleep(2)

    def create_layout(self):
        # ==========================================
        # HEADER (TOP BAR)
        # ==========================================
        header_frame = tk.Frame(self.root, bg=self.colors["header"], height=80)
        header_frame.pack(fill="x", side="top")
        header_frame.pack_propagate(False)

        title_lbl = tk.Label(header_frame, text="🏥 MEDICAL IoT: ARQUITECTURA LAMBDA", 
                             font=self.fonts["title"], bg=self.colors["header"], fg=self.colors["accent"])
        title_lbl.pack(side="left", padx=20, pady=10)
        
        subtitle_lbl = tk.Label(header_frame, text="Centro de Aprendizaje e Inferencia en Tiempo Real", 
                                font=self.fonts["desc"], bg=self.colors["header"], fg="#64748b")
        subtitle_lbl.pack(side="left", pady=15)

        # Live telemetry counters
        stats_frame = tk.Frame(header_frame, bg=self.colors["header"])
        stats_frame.pack(side="right", padx=20, pady=15)

        tk.Label(stats_frame, text="LATIDOS ENVIADOS:", font=self.fonts["btn"], bg=self.colors["header"], fg="#94a3b8").pack(side="left")
        tk.Label(stats_frame, textvariable=self.counters["SENSOR"], font=self.fonts["title"], bg=self.colors["header"], fg=self.colors["success"]).pack(side="left", padx=(5, 20))
        
        tk.Label(stats_frame, text="ARRITMIAS DETECTADAS:", font=self.fonts["btn"], bg=self.colors["header"], fg="#94a3b8").pack(side="left")
        tk.Label(stats_frame, textvariable=self.counters["ANOMALIES"], font=self.fonts["title"], bg=self.colors["header"], fg=self.colors["danger"]).pack(side="left", padx=5)

        # ==========================================
        # INFRASTRUCTURE STATUS BAR
        # ==========================================
        self.infra_bar = tk.Frame(self.root, bg="#111827", height=35)
        self.infra_bar.pack(fill="x")
        self.infra_bar.pack_propagate(False)
        
        tk.Label(self.infra_bar, text="🔌 ESTADO DE SERVICIOS (Docker Stack):", font=self.fonts["btn"], bg="#111827", fg="#94a3b8").pack(side="left", padx=(20, 10))
        
        self.infra_leds = {}
        for name in self.infra_status.keys():
            frame = tk.Frame(self.infra_bar, bg="#111827")
            frame.pack(side="left", padx=15)
            
            canvas = tk.Canvas(frame, width=10, height=10, bg="#111827", highlightthickness=0)
            canvas.pack(side="left", padx=(0, 5))
            led = canvas.create_oval(2, 2, 8, 8, fill=self.colors["danger"])
            self.infra_leds[name] = (canvas, led)
            
            tk.Label(frame, text=name, font=self.fonts["console"], bg="#111827", fg="#cbd5e1").pack(side="left")

        # ==========================================
        # TOOLBAR
        # ==========================================
        toolbar = tk.Frame(self.root, bg=self.colors["bg"], pady=8)
        toolbar.pack(fill="x", padx=20)

        tk.Button(toolbar, text="🛑 DETENER TODOS LOS PROCESOS", command=self.stop_all, bg=self.colors["danger"], fg="white", font=self.fonts["btn"], relief="flat", padx=15, pady=4).pack(side="left")
        
        tk.Button(toolbar, text="🧠 MLflow Dashboard (Registro)", command=lambda: webbrowser.open("http://localhost:5001"), bg="#4f46e5", fg="white", font=self.fonts["btn"], relief="flat", padx=15, pady=4).pack(side="right", padx=5)
        tk.Button(toolbar, text="📊 Grafana Realtime Monitor", command=lambda: webbrowser.open("http://localhost:3000"), bg="#ea580c", fg="white", font=self.fonts["btn"], relief="flat", padx=15, pady=4).pack(side="right", padx=5)
        tk.Button(toolbar, text="🔌 Swagger API Docs", command=lambda: webbrowser.open("http://localhost:8000/docs"), bg="#059669", fg="white", font=self.fonts["btn"], relief="flat", padx=15, pady=4).pack(side="right")

        # ==========================================
        # PIPELINE COLUMNS (Lambda Architecture Flow)
        # ==========================================
        pipeline_frame = tk.Frame(self.root, bg=self.colors["bg"])
        pipeline_frame.pack(fill="both", expand=True, padx=15, pady=5)

        # 4 Columns definitions representing:
        # Col 0: Data & Training
        # Col 1: Speed Layer
        # Col 2: Batch Layer
        # Col 3: Serving Layer
        columns_info = [
            {"title": "📡 ORIGEN Y PREPARACIÓN", "desc": "Ingesta de datos y preparación de IA", "color": self.colors["success"]},
            {"title": "⚡ SPEED LAYER (REALTIME)", "desc": "Detección inmediata en milisegundos", "color": self.colors["warning"]},
            {"title": "🗄️ BATCH LAYER (HISTÓRICO)", "desc": "Almacén inmutable y agregación diaria", "color": self.colors["batch"]},
            {"title": "🌐 SERVING LAYER (REST API)", "desc": "Vista unificada consolidada para consulta", "color": self.colors["serving"]}
        ]

        self.columns = []
        for i, col_data in enumerate(columns_info):
            col_frame = tk.LabelFrame(pipeline_frame, text=col_data["title"], font=self.fonts["subtitle"], 
                                      bg="#0f172a", fg=col_data["color"], bd=1, labelanchor="n", padx=5, pady=5)
            col_frame.grid(row=0, column=i, sticky="nsew", padx=8, pady=5)
            pipeline_frame.columnconfigure(i, weight=1)
            
            # Column Subtitle description
            tk.Label(col_frame, text=col_data["desc"], font=self.fonts["desc"], bg="#0f172a", fg="#64748b").pack(fill="x", pady=(0, 8))
            
            self.columns.append(col_frame)
            
        pipeline_frame.rowconfigure(0, weight=1)

        # Define modules and map them to their corresponding columns
        self.modules = {
            "TRAIN": {
                "path": "batch/train_model.py",
                "name": "1. Pre-Entrenamiento",
                "col": 0,
                "color": self.colors["accent"],
                "desc": "Entrena el modelo de IA Isolation Forest usando datos clínicos sanos de referencia y los guarda en MLflow."
            },
            "SENSOR": {
                "path": "data_sources/sensor_simulador.py",
                "name": "2. Sensor Holter (ECG)",
                "col": 0,
                "color": self.colors["success"],
                "desc": "Simula la transmisión constante de electrocardiogramas desde el paciente hacia Kafka."
            },
            "DETECT": {
                "path": "streaming/anomaly_detector.py",
                "name": "3B. Detector de Arritmias",
                "col": 1,
                "color": self.colors["warning"],
                "desc": "Speed Layer: Consume ECGs vivos, realiza inferencia latido a latido con MLflow y guarda alarmas instantáneas."
            },
            "LAKE": {
                "path": "streaming/raw_to_datalake.py",
                "name": "3A. Ingesta a Data Lake",
                "col": 2,
                "color": self.colors["accent"],
                "desc": "Batch Ingest: Copia de forma inmutable y cronológica todos los datos a archivos JSONL diarios (Master Dataset)."
            },
            "BATCH": {
                "path": "batch/scheduler.py",
                "name": "4. Orquestador Batch",
                "col": 2,
                "color": self.colors["batch"],
                "desc": "Procesamiento Batch: Lee todo el Data Lake inmutable periódicamente para consolidar resúmenes exactos en Postgres."
            },
            "SERVING": {
                "path": "serving/query_api.py",
                "name": "5. Query API RESTful",
                "col": 3,
                "color": self.colors["serving"],
                "desc": "Serving Layer: Expone FastAPI uniendo datos históricos de Batch con alertas de Speed Layer (Merge Lambda)."
            }
        }

        self.consoles = {}
        self.leds = {}

        # Render module cards into columns
        for key, info in self.modules.items():
            self.create_module_card(self.columns[info["col"]], key, info)

    def create_module_card(self, parent, key, info):
        """Creates an educational card with info, controls, and an output console"""
        card = tk.Frame(parent, bg=self.colors["panel"], bd=0)
        card.pack(fill="both", expand=True, padx=5, pady=6)

        # Header bar of the card
        header = tk.Frame(card, bg=self.colors["panel"])
        header.pack(fill="x", padx=8, pady=(8, 2))

        # LED Status indicator
        led_canvas = tk.Canvas(header, width=12, height=12, bg=self.colors["panel"], highlightthickness=0)
        led_canvas.pack(side="left", pady=2)
        self.leds[key] = led_canvas.create_oval(2, 2, 10, 10, fill="#475569") # Grey (off)

        # Title
        tk.Label(header, text=info["name"], font=self.fonts["subtitle"], bg=self.colors["panel"], fg=info["color"]).pack(side="left", padx=5)

        # Help button for student guidance
        btn_help = tk.Button(header, text="❔", command=lambda: messagebox.showinfo(info["name"], info["desc"]), 
                             bg=self.colors["panel"], fg="#94a3b8", relief="flat", font=self.fonts["desc"])
        btn_help.pack(side="right")

        # Action controls
        ctrl = tk.Frame(card, bg=self.colors["panel"])
        ctrl.pack(fill="x", padx=8, pady=4)
        
        btn_start = tk.Button(ctrl, text="▶ INICIAR", command=lambda k=key: self.start_proc(k), bg="#334155", fg="white", relief="flat", font=self.fonts["btn"], width=10)
        btn_start.pack(side="left", padx=2)
        
        btn_stop = tk.Button(ctrl, text="⏹ DETENER", command=lambda k=key: self.stop_proc(k), bg="#334155", fg="white", relief="flat", font=self.fonts["btn"], width=10)
        btn_stop.pack(side="left", padx=2)

        btn_clear = tk.Button(ctrl, text="🗑 LIMPIAR", command=lambda k=key: self.clear_console(k), bg="#334155", fg="#cbd5e1", relief="flat", font=self.fonts["btn"])
        btn_clear.pack(side="right", padx=2)

        # Output console
        console = scrolledtext.ScrolledText(card, bg="#020617", fg="#10b981", font=self.fonts["console"], state="disabled", bd=0, padx=5, pady=5, height=8)
        console.pack(fill="both", expand=True, padx=8, pady=(0, 8))
        
        console.tag_config("ERROR", foreground=self.colors["danger"])
        console.tag_config("SYSTEM", foreground=self.colors["accent"])
        console.tag_config("ALERT", foreground=self.colors["warning"], background="#451a03")
        
        self.consoles[key] = console

    # ==========================================
    # LOGIC & THREAD MANAGEMENT
    # ==========================================
    def log(self, key, text, tag=None):
        self.msg_queue.put((key, text, tag))

    def update_loop(self):
        """Safely processes logs and health updates from background threads"""
        while not self.msg_queue.empty():
            key, text, tag = self.msg_queue.get()
            
            # Port checking signals
            if key == "INFRA_UPDATE":
                for name, status in self.infra_status.items():
                    canvas, led = self.infra_leds[name]
                    color = self.colors["success"] if status else self.colors["danger"]
                    canvas.itemconfig(led, fill=color)
                continue

            # Real-time counter updates
            if "Enviando segundo" in text:
                try:
                    parts = text.split("|")
                    if len(parts) > 1 and "latidos transmitidos" in parts[1]:
                        count = int(parts[1].replace("latidos transmitidos", "").strip())
                        self.counters["SENSOR"].set(count)
                    else:
                        self.counters["SENSOR"].set(self.counters["SENSOR"].get() + 100)
                except Exception:
                    self.counters["SENSOR"].set(self.counters["SENSOR"].get() + 100)
            if "🚨 ANOMALÍA" in text:
                self.counters["ANOMALIES"].set(self.counters["ANOMALIES"].get() + 1)
                tag = "ALERT"
            if "Error" in text or "Exception" in text or "[ERR]" in text or "NoBrokersAvailable" in text:
                tag = "ERROR"

            if key in self.consoles:
                c = self.consoles[key]
                c.config(state="normal")
                if tag:
                    c.insert(tk.END, f"{text}\n", tag)
                else:
                    c.insert(tk.END, f"{text}\n")
                c.see(tk.END)
                c.config(state="disabled")
        
        self.root.after(50, self.update_loop)

    def set_led(self, key, is_on):
        """Sets the script running indicator LED color"""
        color = self.modules[key]["color"] if is_on else "#475569"
        canvas = self.leds[key]
        # Tkinter Canvas parent lookup helper
        for child in self.root.winfo_children():
            self._update_led_recursive(child, key, color)

    def _update_led_recursive(self, widget, key, color):
        if isinstance(widget, tk.Canvas):
            items = widget.find_all()
            if items and items[0] == self.leds[key]:
                widget.itemconfig(items[0], fill=color)
                return
        for child in widget.winfo_children():
            self._update_led_recursive(child, key, color)

    def start_proc(self, key):
        if key in self.processes:
            self.log(key, f"⚠️ El proceso ya está en ejecución.", "SYSTEM")
            return
        
        # Educational hint: Warn the student if dependent services are offline
        if key in ["SENSOR", "LAKE", "DETECT"] and not self.infra_status["Kafka (9092)"]:
            messagebox.showwarning("Falta Infraestructura", 
                                  "¡Kafka (puerto 9092) no está disponible!\n\nAsegúrate de haber levantado el contenedor docker:\n'docker-compose up -d'")
        
        if key == "DETECT" and not self.infra_status["MLflow (5001)"]:
            messagebox.showwarning("Falta Infraestructura", 
                                  "¡MLflow (puerto 5001) no está activo!\n\nSe requiere MLflow para descargar el modelo entrenado en la Speed Layer.")

        path = self.modules[key]["path"]
        if not os.path.exists(path):
            self.log(key, f"❌ Archivo no encontrado: {path}", "ERROR")
            return

        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8" # Fix emojis encoding in Windows
        
        try:
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

            p = subprocess.Popen([sys.executable, "-u", path], 
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 text=True, encoding='utf-8', env=env, startupinfo=startupinfo)
            self.processes[key] = p
            self.set_led(key, True)
            self.log(key, f"▶ INICIANDO: {self.modules[key]['name']}", "SYSTEM")

            threading.Thread(target=self.stream_watcher, args=(p.stdout, key), daemon=True).start()
            threading.Thread(target=self.stream_watcher, args=(p.stderr, key, "[ERR] "), daemon=True).start()
            threading.Thread(target=self.wait_proc, args=(p, key), daemon=True).start()

        except Exception as e:
            self.log(key, f"❌ Error al iniciar subproceso: {e}", "ERROR")

    def stream_watcher(self, stream, key, prefix=""):
        for line in iter(stream.readline, ''):
            if line: 
                self.log(key, f"{prefix}{line.strip()}")
        stream.close()

    def wait_proc(self, p, key):
        p.wait()
        if key in self.processes:
            del self.processes[key]
            self.set_led(key, False)
            self.log(key, f"⏹ PROCESO FINALIZADO (Cerrado)", "SYSTEM")

    def stop_proc(self, key):
        if key in self.processes:
            self.processes[key].terminate()

    def stop_all(self):
        for key in list(self.processes.keys()):
            self.stop_proc(key)

    def clear_console(self, key):
        self.consoles[key].config(state="normal")
        self.consoles[key].delete('1.0', tk.END)
        self.consoles[key].config(state="disabled")

    def on_close(self):
        self.infra_running = False
        self.stop_all()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = LambdaCommandCenter(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()