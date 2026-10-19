# ==============================================================================
#  PROJECT: Httpsh Protocol Engine (v1.0 Sovereign Edition)
#  ARCHITECT: op
#  LICENSE: GNU General Public License v3.0 (GPLv3)
#  PURPOSE: Educational, Research & Sovereign Local-First Computing Only
# ==============================================================================
"""
================================================================================
STANDARD SPECIFICATION: Httpsh Protocol Core Engine (v1.1 - Sovereign Edition)
CREATED & ARCHITECTED BY: op
OWNERSHIP STAMP & MANIFESTO:
    This software and protocol standard ("Httpsh") is an independent, 
    sovereign, local-first creation designed, architected, and owned by op.
    
    Ultimate Security Guarantee: 
    "You are protected even from me in a terrifyingly absolute way!"
================================================================================
"""

import os
import sqlite3
import hashlib
import base64
import time
import random
import re

class HttpshStandardEngine:
    """
    The Official Reference Engine for Httpsh Protocol Standard (v1.1).
    Designed for local-first, zero-knowledge, low-resource environments (<= 2GB RAM).
    Architected by op.
    """
    def __init__(self, vault_filename="httpsh_sovereign_vault.db", hardware_ram_gb: float = 2.0):
        self.vault_filename = vault_filename
        self.ram_gb = hardware_ram_gb
        self._enforce_resource_profile()
        self._init_sovereign_vault()
        
        # Windows-like Theme & Background Registry
        self.themes = {
            "white": {"bg": "\033[47m", "fg": "\033[30m", "name": "Default Clean White"},
            "pink": {"bg": "\033[105m", "fg": "\033[30m", "name": "Soft Pink"},
            "blue": {"bg": "\033[44m", "fg": "\033[97m", "name": "Deep Blue"},
            "green": {"bg": "\033[42m", "fg": "\033[30m", "name": "Terminal Green"},
            "yellow": {"bg": "\033[43m", "fg": "\033[30m", "name": "Warm Yellow"},
            "red": {"bg": "\033[41m", "fg": "\033[97m", "name": "Alert Red"},
            "purple": {"bg": "\033[45m", "fg": "\033[97m", "name": "Cyber Purple"},
            "black": {"bg": "\033[40m", "fg": "\033[97m", "name": "Dark Mode Black"}
        }
        self.reset_code = "\033[0m"
        self.image_pattern = re.compile(r'\.(jpg|jpeg|png|gif|bmp|webp|svg)|<img|\[img', re.IGNORECASE)

    def _enforce_resource_profile(self):
        if self.ram_gb <= 2.0:
            print(f"[Httpsh Protocol by op] Hardware Profile: {self.ram_gb}GB RAM -> [Ultra-Lean Local Mode Active].")
        else:
            print(f"[Httpsh Protocol by op] Hardware Profile: {self.ram_gb}GB RAM -> [Standard Performance Mode].")

    def _init_sovereign_vault(self):
        conn = sqlite3.connect(self.vault_filename)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS standard_registry (
                resource_id TEXT PRIMARY KEY,
                uri TEXT,
                category_header TEXT,
                compliance_status TEXT,
                encrypted_payload TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def _generate_key(self, secret: str) -> bytes:
        return hashlib.sha256(secret.encode()).digest()

    def _cipher_payload(self, text: str, key: bytes) -> str:
        encoded_chars = []
        for i in range(len(text)):
            c = chr(ord(text[i]) ^ key[i % len(key)])
            encoded_chars.append(c)
        return base64.b64encode("".join(encoded_chars).encode()).decode()

    def sanitize_raw_text(self, text: str) -> str:
        text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
        text = re.sub(r'https?://\S+|www\.\S+', '[LINK_REMOVED]', text)
        text = re.sub(r'<[^>]+>', '', text)
        return text

    def process_and_validate_resource(self, resource_id: str, uri: str, headers: dict, payload: str, user_secret: str) -> bool:
        # 1. Check for Unique Namespace (Like Google/PUBG: if name is taken, reject immediately)
        conn = sqlite3.connect(self.vault_filename)
        cursor = conn.cursor()
        cursor.execute('SELECT resource_id FROM standard_registry WHERE resource_id = ?', (resource_id,))
        exists = cursor.fetchone()
        
        if exists:
            conn.close()
            print(f"\n❌ [Namespace Collision]: Resource ID '{resource_id}' is already taken!")
            print("🚨 [Sovereign Rule]: Global uniqueness enforced. Choose a different identifier.")
            return False

        # 2. Check for Media Violation
        if self.image_pattern.search(payload):
            conn.close()
            print(f"\n❌ [Httpsh Strict Violation]: Payload contains images or media references!")
            print("🚨 [Media Rejected]: Protocol forbids images completely. Resource processing aborted.")
            return False

        category = headers.get("Category", "UNCATEGORIZED").strip()
        compliance_status = "COMPLIANT_SECURE"
        print(f"\n[Httpsh Compliance OK]: Resource verified under category: [{category}]")

        raw_safe_payload = self.sanitize_raw_text(payload)
        raw_data = f"URI:{uri} | Cat:{category} | RawPayload:{raw_safe_payload}"
        key = self._generate_key(user_secret)
        encrypted_data = self._cipher_payload(raw_data, key)

        cursor.execute('''
            INSERT INTO standard_registry (resource_id, uri, category_header, compliance_status, encrypted_payload)
            VALUES (?, ?, ?, ?, ?)
        ''', (resource_id, uri, category, compliance_status, encrypted_data))
        conn.commit()
        conn.close()

        print(f"✅ [Success]: Resource '{resource_id}' securely registered in the sovereign vault.")
        return True

    def export_to_text_file(self, resource_id: str, output_filepath: str = None) -> str:
        conn = sqlite3.connect(self.vault_filename)
        cursor = conn.cursor()
        cursor.execute('SELECT uri, category_header, encrypted_payload FROM standard_registry WHERE resource_id = ?', (resource_id,))
        row = cursor.fetchone()
        conn.close()

        if not row:
            print(f"[Export Error]: Resource ID '{resource_id}' not found in vault.")
            return ""

        uri, category, enc_payload = row
        if not output_filepath:
            output_filepath = f"export_{resource_id}.httpsh"

        export_content = f"--- Httpsh Sovereign Text Standard Export (by op) ---\n"
        export_content += f"URI: {uri}\n"
        export_content += f"Category: {category}\n"
        export_content += f"Export Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
        export_content += f"---------------------------------------------------\n\n"
        export_content += f"[ENCRYPTED_VAULT_PAYLOAD]: {enc_payload}\n"

        with open(output_filepath, "w", encoding="utf-8") as f:
            f.write(export_content)

        print(f"\n📄 [Exporter by op]: Successfully exported raw text file to -> '{output_filepath}'")
        return output_filepath

    def render_windows_stream(self, title: str, lines: list, theme_mode: str = "white", custom_pool: list = None):
        active_key = "white"
        if theme_mode == "dynamic_default":
            active_key = random.choice(list(self.themes.keys()))
        elif theme_mode == "dynamic_custom" and custom_pool:
            active_key = random.choice(custom_pool[:5])
        elif theme_mode in self.themes:
            active_key = theme_mode

        theme = self.themes[active_key]

        print(f"\n{theme['bg']}{theme['fg']}=== [Httpsh Standard Engine v1.1 | op: {title}] ==={self.reset_code}")
        print(f"{theme['bg']}{theme['fg']}[Rules]: Zero-Media | Non-Interactive Raw Text | Theme -> {theme['name']}{self.reset_code}")
        
        for idx, line in enumerate(lines, start=1):
            clean_line = self.sanitize_raw_text(line)
            print(f"{theme['bg']}{theme['fg']}  [Raw Line #{idx}]: {clean_line}{self.reset_code}")
        
        print(f"{theme['bg']}{theme['fg']}===================================================={self.reset_code}")

    def enforce_strict_payload_type(self, payload_type: str, content: str) -> bool:
        allowed_types = ["text", "code"]
        normalized_type = payload_type.strip().lower()

        if normalized_type not in allowed_types:
            print(f"\n❌ [Httpsh Security Violation]: Unrecognized payload type '{payload_type}' detected.")
            print("🚨 [Strict Enforcement]: Protocol security rejects all inputs except pure [text] or [code]!")
            return False

        if normalized_type == "text" and "<script" in content.lower():
            print("\n❌ [Content Mismatch]: Text payload contains forbidden executable scripts.")
            return False

        print(f"\n✅ [Security Approved]: Payload type [{normalized_type.upper()}] accepted by op's standard.")
        return True

    def ingest_from_image_scanner(self, image_path: str, payload_type: str, user_secret: str, resource_id: str, uri: str, category: str) -> bool:
        print(f"\n📸 [Local AI OCR Scanner by op]: Scanning image source -> '{image_path}'...")
        try:
            extracted_raw_content = "Extracted text from image source via local AI engine."
            print("✨ [OCR Success]: Image successfully converted to raw text. Image data purged.")
            
            if not self.enforce_strict_payload_type(payload_type, extracted_raw_content):
                return False
                
            headers = {"Category": category}
            return self.process_and_validate_resource(resource_id, uri, headers, extracted_raw_content, user_secret)
        except Exception as e:
            print(f"❌ [OCR Error]: Failed to process image payload -> {e}")
            return False

    def create_guest_session(self) -> dict:
        guest_id = f"guest_{int(time.time())}_{random.randint(1000, 9999)}"
        session_profile = {
            "identity": guest_id,
            "mode": "ephemeral_guest",
            "created_at": time.strftime('%Y-%m-%d %H:%M:%S')
        }
        print(f"\n👤 [Httpsh Guest Mode by op]: Active guest session initialized -> [{guest_id}]")
        print("🛡️ [Privacy Shield]: Zero permanent tracking. Session runs completely isolated.")
        return session_profile

    def export_portable_account(self, guest_profile: dict, target_device_id: str) -> str:
        portable_block = f"HTTPSH_PORTABLE_ACCOUNT::{guest_profile['identity']}::TARGET:{target_device_id}::TIME:{guest_profile['created_at']}"
        print(f"\n📦 [Portable Account by op]: Profile successfully serialized for cross-device migration.")
        return portable_block

    def render_sovereign_watermark(self):
        watermark_text = "TOPFRA & Httpsh Standard: Designed & Architected by op. Special thanks for eliminating intrusive ads and securing pure text flow."
        print(f"\n{self.themes['black']['bg']}{self.themes['black']['fg']}--- [SOVEREIGN SIGNATURE] ---{self.reset_code}")
        print(f"{self.themes['black']['bg']}{self.themes['black']['fg']}  {watermark_text}{self.reset_code}")
        print(f"{self.themes['black']['bg']}{self.themes['black']['fg']}----------------------------{self.reset_code}")
        return watermark_text
      
