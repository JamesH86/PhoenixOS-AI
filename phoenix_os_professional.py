#!/usr/bin/env python3
import sys, os, subprocess, webbrowser, json, time, random, psutil, platform
from datetime import datetime
from PyQt5.QtWidgets import *; from PyQt5.QtCore import *; from PyQt5.QtGui import *

# --- AI Imports ---
from openai import OpenAI
# --- END AI Imports ---

# --- DEPENDENCY CHECK ---
def check_dependencies():
    required_modules = ['psutil', 'PyQt5', 'openai']
    missing_modules = []
    for module in required_modules:
        try:
            if module == 'openai': from openai import OpenAI as _temp_openai_check
            else: __import__(module)
        except ImportError: missing_modules.append(module)
    if missing_modules: print(f'Phoenix: Missing dependencies: {", ".join(missing_modules)}. Install with pip install -r requirements.txt'); sys.exit(1)
check_dependencies()
# --- End DEPENDENCY CHECK ---

class PhoenixCore:
    def __init__(self):
        self.os_info = platform.system()
        self.openai_client = None
        if os.getenv('OPENAI_API_KEY'):
            try: self.openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY')); self.openai_client.chat.completions.create(model='gpt-3.5-turbo', messages=[{'role':'user','content':'test'}], max_tokens=5); print('Phoenix: OpenAI API: ACTIVE')
            except Exception as e: print(f'Phoenix: OpenAI API Error: {e}')
        else: print('Phoenix: OpenAI API: OFFLINE (no key)')
        
        self.local_ai_responses = {
            'hello': ['Yo! Phoenix here, ready to dominate!', 'What\'s good, boss? Ready for some cyber warfare!', 'Phoenix online! Let\'s break some systems!'],
            'scan': ['Initiating advanced network reconnaissance...', 'Scanning for open ports and services...', 'Vulnerability assessment in progress!'],
            'exploit': ['Exploitation sequence activated! System compromise imminent!', 'Deploying advanced payloads...', 'Authentication bypass successful!'],
            'status': [f'Phoenix OS Status: OS: {self.os_info}, CPU: {psutil.cpu_percent()}%, Memory: {psutil.virtual_memory().percent}%', 'All systems operational and ready for action!', 'Phoenix Core: ACTIVE. Security modules loaded.'],
            'money': ['Phoenix: Opening Monetization Suite...', 'Accessing bug bounty platforms...', 'Generating freelance leads...'],
            'default': ['Phoenix AI: Processing your command with local intelligence.', 'Analyzing query... Command executed.', 'Ready for the next cyber operation!']
        }

    def get_ai_response(self, prompt):
        if self.openai_client:
            try: return self.openai_client.chat.completions.create(model='gpt-3.5-turbo', messages=[{'role':'system','content':'You are Phoenix, an AI cybersecurity assistant. Provide concise, badass, and technical advice.'},{'role':'user','content':prompt}], max_tokens=200).choices[0].message.content.strip()
            except Exception as e: return f'🤖 OpenAI Error: {e}'
        return f'🤖 No AI active. Processing locally: {prompt}'

    def get_local_ai_response(self, prompt):
        prompt_lower = prompt.lower()
        if "hello" in prompt_lower or "hi" in prompt_lower: return random.choice(self.local_ai_responses['hello'])
        elif "scan" in prompt_lower: return random.choice(self.local_ai_responses['scan'])
        elif "exploit" in prompt_lower or "hack" in prompt_lower: return random.choice(self.local_ai_responses['exploit'])
        elif "status" in prompt_lower or "how are you" in prompt_lower: return random.choice(self.local_ai_responses['status'])
        elif "money" in prompt_lower or "monetization" in prompt_lower: return random.choice(self.local_ai_responses['money'])
        return random.choice(self.local_ai_responses['default'])

    def process_command(self, command):
        cmd = command.lower().strip()
        if cmd in ['help', '?']: return 'Phoenix OS Commands: scan <target>, exploit <target>, phoenix_cyber_mode, money, status, files, settings, clear, exit. You can also ask me questions naturally!'
        elif cmd.startswith('scan '): return f'Phoenix Scanner: {cmd.split(" ",1)[1]} - Scan complete!'
        elif cmd.startswith('exploit '): return f'Phoenix Exploitation: {cmd.split(" ",1)[1]} - System compromise imminent!'
        elif cmd in ['phoenix_cyber_mode', 'cyber mode']: return 'Phoenix Cybersecurity Mode ACTIVATED!'
        elif cmd in ['money', 'monetization']: return '💰 Phoenix: Opening Monetization Suite...'
        elif cmd == 'status': return f'📊 Phoenix OS Status: OS: {self.os_info}, CPU: {psutil.cpu_percent()}%, Memory: {psutil.virtual_memory().percent}%'
        elif cmd == 'files': return '📁 Opening File Manager...'
        elif cmd == 'settings': return '⚙️ Opening Settings Panel...'
        elif cmd == 'clear': return 'CLEAR_TERMINAL'
        elif cmd in ['exit', 'quit']: return 'TERMINAL_EXIT'
        else:
            ai_response = self.get_ai_response(command)
            if 'OpenAI Error' in ai_response or 'No AI active' in ai_response: return f'Phoenix (Local AI): {self.get_local_ai_response(command)}'
            else: return f'Phoenix (OpenAI): {ai_response}'

class PhoenixMenuBar(QMenuBar):
    def __init__(self, parent):
        super().__init__(parent); self.setStyleSheet('QMenuBar {background: #2b2b2b; color: #ffffff;border-bottom: 1px solid #555555;font-size: 11px;padding: 2px;} QMenuBar::item {background: transparent;padding: 4px 12px;} QMenuBar::item:selected {background: #ff6b35;color: white;} QMenu {background: #2b2b2b;color: #ffffff;border: 1px solid #555555;} QMenu::item:selected {background: #ff6b35;}'); self.create_menus()
    def create_menus(self):
        apps_menu = self.addMenu('Applications'); phoenix_tools_menu = apps_menu.addMenu('Phoenix Tools'); phoenix_tools_menu.addAction('Terminal', self.parent().show_terminal); phoenix_tools_menu.addAction('Phoenix Cyber Mode', self.parent().launch_cyber_mode); phoenix_tools_menu.addAction('Monetization Suite', self.parent().launch_monetization); phoenix_tools_menu.addAction('Security Scanner', self.parent().launch_scanner); system_menu = apps_menu.addMenu('System'); system_menu.addAction('File Manager', self.parent().launch_files); system_menu.addAction('Settings', self.parent().show_settings); system_menu.addAction('Web Browser', lambda: webbrowser.open('https://github.com/JamesH86/PhoenixOS-AI')); system_menu.addAction('Trash Can', self.parent().launch_trash); tools_menu = self.addMenu('Tools'); tools_menu.addAction('Network Scanner', self.parent().launch_scanner); tools_menu.addAction('Security Audit', self.parent().launch_cyber_mode); tools_menu.addAction('Wireless Attacks', self.parent().launch_wireless); tools_menu.addAction('Web Tunneling', self.parent().launch_web_tunneling); tools_menu.addAction('Tor Browser', self.parent().launch_tor); system_menu = self.addMenu('System'); system_menu.addAction('Settings', self.parent().show_settings); system_menu.addAction('System Monitor', self.parent().show_system_monitor); system_menu.addAction('Restart', self.parent().restart_phoenix); system_menu.addAction('Shutdown', self.parent().close)

class PhoenixTaskbar(QWidget):
    def __init__(self, parent):
        super().__init__(parent); self.setFixedHeight(35); self.setStyleSheet('QWidget {background: #2b2b2b;border-top: 1px solid #555555;}'); layout = QHBoxLayout(); layout.setContentsMargins(8, 2, 8, 2); self.launcher = QPushButton('Phoenix'); self.launcher.setFixedSize(80, 30); self.launcher.setStyleSheet('QPushButton {background: #ff6b35;color: white;border: none;border-radius: 15px;font-weight: bold;font-size: 11px;} QPushButton:hover {background: #ff8c42;}'); self.launcher.clicked.connect(parent.show_launcher_menu); layout.addWidget(self.launcher); layout.addStretch(); self.system_info_label = QLabel('Phoenix OS'); self.system_info_label.setStyleSheet('color: #88c0d0; font-size: 10px;'); layout.addWidget(self.system_info_label); self.time_label = QLabel(); self.time_label.setStyleSheet('color: #ffffff; font-size: 11px; font-weight: bold;'); layout.addWidget(self.time_label); self.setLayout(layout); self.timer_time = QTimer(); self.timer_time.timeout.connect(self.update_time); self.timer_time.start(1000); self.update_time()
    def update_time(self): current_time = datetime.now().strftime('%H:%M  %m/%d'); self.time_label.setText(current_time)

class PhoenixTerminal(QWidget):
    def __init__(self, phoenix_core):
        super().__init__(parent=None); self.phoenix = phoenix_core; self.setWindowTitle('Phoenix Terminal'); self.setGeometry(150, 150, 900, 600); self.setStyleSheet('QWidget {background: #1e1e1e;color: #ffffff;}'); layout = QVBoxLayout(); layout.setContentsMargins(0, 0, 0, 0); self.output = QTextEdit(); self.output.setReadOnly(True); self.output.setStyleSheet('QTextEdit {background: #1e1e1e;color: #00ff00;border: none;font-family: \'Courier New\', monospace;font-size: 12px;padding: 10px;}'); welcome = f'Phoenix OS Terminal v2.0\\nCore AI: ACTIVE | Security: ONLINE | Monetization: READY\\nType \'help\' for commands or start with: scan, exploit, phoenix_cyber_mode, money, aws list buckets\\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\\n'; self.output.append(welcome); input_area = QWidget(); input_area.setStyleSheet('background: #2b2b2b; padding: 5px;'); input_layout = QHBoxLayout(); prompt = QLabel('phoenix@os:~$'); prompt.setStyleSheet('color: #ff6b35; font-weight: bold; font-family: \'Courier New\';'); self.input = QLineEdit(); self.input.setStyleSheet('QLineEdit {background: transparent;color: #ffffff;border: none;font-family: \'Courier New\', monospace;font-size: 12px;}'); self.input.returnPressed.connect(self.process_command); input_layout.addWidget(prompt); input_layout.addWidget(self.input); input_area.setLayout(input_layout); layout.addWidget(self.output); layout.addWidget(input_area); self.setLayout(layout); self.input.setFocus()
    def process_command(self):
        command = self.input.text().strip(); self.output.append(f'phoenix@os:~$ {command}'); response = self.phoenix.process_command(command)
        if response == 'CLEAR_TERMINAL': self.output.clear(); self.output.append(f'Phoenix OS Terminal v2.0\\nCore AI: ACTIVE | Security: ONLINE | Monetization: READY\\nType \'help\' for commands or start with: scan, exploit, phoenix_cyber_mode, money, aws list buckets\\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\\n')
        elif response == 'TERMINAL_EXIT': self.close()
        elif response.startswith('💰 Phoenix: Opening Monetization Suite...'): self.parent().launch_monetization(); self.output.append(response)
        elif response.startswith('📁 Opening File Manager...'): self.parent().launch_files(); self.output.append(response)
        elif response.startswith('⚙️ Opening Settings Panel...'): self.parent().show_settings(); self.output.append(response)
        else: self.output.append(response); self.output.append(''); self.input.clear(); scrollbar = self.output.verticalScrollBar(); scrollbar.setValue(scrollbar.maximum())
    def open_file_manager(self):
        if sys.platform == 'darwin': subprocess.run(['open', '.'])
        elif sys.platform == 'linux': subprocess.run(['nautilus', '.'])
        else: subprocess.run(['explorer', '.'])

class PhoenixDesktop(QMainWindow):
    def __init__(self):
        super().__init__(); self.phoenix = PhoenixCore(); self.setWindowTitle('🔥 Phoenix OS - Professional Cybersecurity Desktop'); self.setGeometry(100, 100, 1200, 800); self.setWindowIcon(QIcon()); self.init_desktop(); self.terminal_window = None; self.launcher = QPushButton('Phoenix')
    def init_desktop(self):
        self.central_widget = QWidget(); self.setCentralWidget(self.central_widget); layout = QVBoxLayout(); layout.setContentsMargins(0, 0, 0, 0); layout.setSpacing(0); self.menu_bar = PhoenixMenuBar(self); self.setMenuBar(self.menu_bar); self.desktop_area = QWidget(); self.desktop_area.setStyleSheet('QWidget {background: qlineargradient(x1:0, y1:0, x2:1, y2:1,stop:0 #2e3440, stop:1 #3b4252);}'); desktop_layout = QVBoxLayout(); desktop_layout.setAlignment(Qt.AlignCenter); logo = QLabel('🔥 PHOENIX OS'); logo.setAlignment(Qt.AlignCenter); logo.setStyleSheet('QLabel {color: #88c0d0;font-size: 48px;font-weight: bold;background: transparent;margin: 20px;}'); subtitle = QLabel('Professional Cybersecurity Operating System'); subtitle.setAlignment(Qt.AlignCenter); subtitle.setStyleSheet('QLabel {color: #d8dee9;font-size: 16px;background: transparent;margin-bottom: 30px;}'); button_layout = QHBoxLayout(); button_layout.setAlignment(Qt.AlignCenter); button_layout.setSpacing(20); buttons = [('💻 Terminal', self.show_terminal), ('👑 Cyber Mode', self.launch_cyber_mode), ('💰 Monetization', self.launch_monetization), ('🔍 Scanner', self.launch_scanner)]; [btn.clicked.connect(callback) or button_layout.addWidget(btn) for btn_text, callback in buttons if (btn:=QPushButton(btn_text), btn.setFixedSize(150, 50), btn.setStyleSheet('QPushButton {background: #5e81ac;color: white;border: none;border-radius: 8px;font-size: 12px;font-weight: bold;} QPushButton:hover {background: #81a1c1;} QPushButton:pressed {background: #4c566a;}'))]; desktop_layout.addWidget(logo); desktop_layout.addWidget(subtitle); desktop_layout.addLayout(button_layout); self.desktop_area.setLayout(desktop_layout); layout.addWidget(self.desktop_area); self.taskbar = PhoenixTaskbar(self); layout.addWidget(self.taskbar); self.central_widget.setLayout(layout)
    def show_terminal(self):
        if self.terminal_window is None or not self.terminal_window.isVisible(): self.terminal_window = PhoenixTerminal(self.phoenix); self.terminal_window.show()
        else: self.terminal_window.raise_(); self.terminal_window.activateWindow()
    def launch_cyber_mode(self): QMessageBox.information(self, 'Phoenix', '👑 Phoenix Cybersecurity Mode activated! All security modules online.'); subprocess.Popen([sys.executable, 'phoenix_god_mode.py'])
    def launch_monetization(self): QMessageBox.information(self, 'Phoenix', '💰 Phoenix Monetization Suite launching...'); subprocess.Popen([sys.executable, 'phoenix_monetization_suite.py'])
    def launch_scanner(self): QMessageBox.information(self, 'Phoenix', '🔍 Phoenix Security Scanner online! Ready for reconnaissance.'); subprocess.Popen([sys.executable, 'phoenix_info.py'])
    def launch_voice(self): QMessageBox.information(self, 'Phoenix', '🗣️ Voice control is currently disabled for stability. Please use terminal commands.')
    def launch_files(self): QMessageBox.information(self, 'Phoenix', '📁 Phoenix File Manager opening...'); subprocess.run(['open', '.']) if sys.platform == 'darwin' else subprocess.run(['nautilus', '.']) if sys.platform == 'linux' else subprocess.run(['explorer', '.'])
    def launch_trash(self): QMessageBox.information(self, 'Phoenix', '🗑️ Trash Can opened.'); subprocess.run(['open', '~/.Trash']) if sys.platform == 'darwin' else subprocess.run(['xdg-open', '~/.local/share/Trash']) if sys.platform == 'linux' else subprocess.run(['explorer', 'shell:RecycleBinFolder'])
    def launch_wireless(self): QMessageBox.information(self, 'Phoenix', '📡 Wireless Attack Suite launching...')
    def launch_web_tunneling(self): QMessageBox.information(self, 'Phoenix', '🌐 Web Tunneling options launching...')
    def launch_tor(self): QMessageBox.information(self, 'Phoenix', '🧅 Tor Browser launching...'); webbrowser.open('https://www.torproject.org/download/')
    def show_settings(self):
        dialog = QDialog(self); dialog.setWindowTitle('⚙️ Phoenix OS Settings'); dialog.setFixedSize(500, 400); dialog.setStyleSheet('QDialog {background: #2e3440; color: #eceff4;} QGroupBox {font-weight: bold;border: 2px solid #4c566a;border-radius: 5px;margin: 10px 0;padding-top: 10px;} QGroupBox::title {subcontrol-origin: margin;left: 10px;padding: 0 5px 0 5px;}'); layout = QVBoxLayout(); sys_info_group = QGroupBox('🖥️ System Information'); sys_info_layout = QVBoxLayout(); sys_info_layout.addWidget(QLabel(f'OS: {self.phoenix.os_info}')); sys_info_layout.addWidget(QLabel(f'CPU Cores: {psutil.cpu_count()}')); sys_info_layout.addWidget(QLabel(f'Total Memory: {round(psutil.virtual_memory().total / (1024**3), 2)} GB')); sys_info_group.setLayout(sys_info_layout); layout.addWidget(sys_info_group); phoenix_group = QGroupBox('🔥 Phoenix Core Settings'); phoenix_layout = QVBoxLayout(); settings = [('👑 Phoenix Cyber Mode', True), ('🗣️ Voice Control', False), ('💰 Monetization Suite', True), ('🎯 Auto-scan on boot', False)]; [cb.setChecked(checked) or phoenix_layout.addWidget(cb) for setting, checked in settings if (cb:=QCheckBox(setting))]; phoenix_group.setLayout(phoenix_layout); layout.addWidget(phoenix_group); close_btn = QPushButton('Close'); close_btn.clicked.connect(dialog.close); layout.addWidget(close_btn); dialog.setLayout(layout); dialog.exec_()
    def show_system_monitor(self):
        dialog = QDialog(self); dialog.setWindowTitle('📊 System Monitor'); dialog.setFixedSize(400, 300); dialog.setStyleSheet('QDialog {background: #2e3440; color: #eceff4;} QLabel {font-family: \'Courier New\'; font-size: 11px;}'); layout = QVBoxLayout(); cpu = psutil.cpu_percent(interval=1); memory = psutil.virtual_memory(); info_text = f'📊 SYSTEM MONITOR\\n\\n🖥️ OS: {self.phoenix.os_info}\\n⚡ CPU Usage: {cpu}%\\n🧠 Memory: {memory.percent}%\\n💾 Available RAM: {round(memory.available / (1024**3), 2)}GB\\n🔥 Phoenix Status: ACTIVE\\n\\nReal-time system monitoring active.'; info_label = QLabel(info_text); layout.addWidget(info_label); close_btn = QPushButton('Close'); close_btn.clicked.connect(dialog.close); layout.addWidget(close_btn); dialog.setLayout(layout); dialog.exec_()
    def restart_phoenix(self): reply = QMessageBox.question(self, 'Phoenix OS', 'Restart Phoenix OS?', QMessageBox.Yes | QMessageBox.No); QApplication.quit() if reply == QMessageBox.Yes else None
    def update_system_info_labels(self): pass # Not implemented in this one-liner for simplicity
    def show_launcher_menu(self):
        menu = QMenu(self); menu.setStyleSheet('QMenu {background: #2b2b2b; color: #ffffff; border: 1px solid #555555; font-size: 11px;} QMenu::item:selected {background: #ff6b35;}'); menu.addAction('💻 Terminal', self.show_terminal); menu.addAction('👑 Phoenix Cyber Mode', self.launch_cyber_mode); menu.addAction('💰 Monetization Suite', self.launch_monetization); menu.addAction('🔍 Security Scanner', self.launch_scanner); menu.addSeparator(); menu.addAction('📁 Files', self.launch_files); menu.addAction('⚙️ Settings', self.show_settings); menu.addAction('🌐 Browser', lambda: webbrowser.open('https://github.com/JamesH86/PhoenixOS-AI')); menu.addAction('🗑️ Trash Can', self.launch_trash); menu.addSeparator(); menu.addAction('🔄 Restart', self.restart_phoenix); menu.addAction('⚡ Shutdown', self.close); menu.exec_(self.launcher.mapToGlobal(self.launcher.rect().bottomLeft()))

def main(): app = QApplication(sys.argv); app.setApplicationName('Phoenix OS'); app.setApplicationVersion('2.0'); desktop = PhoenixDesktop(); desktop.showMaximized(); sys.exit(app.exec_())
if __name__ == '__main__': main()
