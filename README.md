# httpsh-protocol
local-first text protocol standard
"""
================================================================================
STANDARD SPECIFICATION: Httpsh Protocol Core Engine (v1.0 - Pure Text & Export Edition)
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
    The Official Reference Engine for Httpsh Protocol Standard (v1.0).
    Designed for local-first, zero-knowledge, low-resource environments (<= 2GB RAM).
    Architected by op.
    
    New Standard Pillars:
    - Pure Raw Text Only (Strips all links, scripts, and interactivity).
    - Strict Zero-Media Filter (Rejects any payload containing images/media).
    - Standard Text File Exporter (Export plain .txt / .httpsh to external clients).
    """
    def __init__(self, vault_filename="httpsh_sovereign_vault.db", hardware_ram_gb: float = 2.0):
        self.vault_filename = vault_filename
        self.ram_gb = hardware_ram_gb
        self._enforce_resource_profile()
        self._init_sovereign_vault()
        
        # Windows-like Theme & Background Registry (Default: Clean White bg / Black text)
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

        # Image extensions & tags filter pattern
        self.image_pattern = re.compile(r'\.(jpg|jpeg|png|gif|bmp|webp|svg)|<img|\[img', re.IGNORECASE)

    def _enforce_resource_profile(self):
        """Standard Rule: Must run smoothly on weak hardware (<= 2GB RAM) with zero background overhead."""
        if self.ram_gb <= 2.0:
            print(f"[Httpsh Protocol by op] Hardware Profile: {self.ram_gb}GB RAM -> [Ultra-Lean Local Mode Active].")
        else:
            print(f"[Httpsh Protocol by op] Hardware Profile: {self.ram_gb}GB RAM -> [Standard Performance Mode].")

    def _init_sovereign_vault(self):
        """Initialize Zero-Knowledge local encrypted SQLite database"""
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
        """
        Rule: Strips all interactive elements (URLs, Markdown links, HTML tags) 
        and converts text into pure non-interactive raw string.
        """
        # Strip URLs and convert markdown links [Text](URL) to plain "Text"
        text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
        text = re.sub(r'https?://\S+|www\.\S+', '[LINK_REMOVED]', text)
        text = re.sub(r'<[^>]+>', '', text) # Strip HTML tags
        return text

    def process_and_validate_resource(self, resource_id: str, uri: str, headers: dict, payload: str, user_secret: str) -> bool:
        """
        Core Standard Compliance Rules:
        1. Reject payload if it contains any image/media references.
        2. Mandatory Category Check (Danger Route if missing).
        3. Convert payload to pure non-interactive raw text.
        """
        # Rule 1: Strict Zero-Media Filter
        if self.image_pattern.search(payload):
            print(f"\n❌ [Httpsh Strict Violation]: Payload contains images or media references!")
            print("🚨 [Media Rejected]: Protocol forbids images completely. Resource processing aborted.")
            return False

        category = headers.get("Category", "").strip()

        if not category:
            print(f"\n[Httpsh Compliance Violation]: Resource '{resource_id}' is missing mandatory 'Category' header.")
            print("🚨 [Standard Enforcement]: Redirecting automatically to the **Dangerous Zone (Hackers Zone)**!")
            compliance_status = "UNTRUSTED_DANGER_ZONE"
        else:
            compliance_status = "COMPLIANT_SECURE"
            print(f"\n[Httpsh Compliance OK]: Resource verified under category: [{category}]")

        # Sanitize text to raw non-interactive format
        raw_safe_payload = self.sanitize_raw_text(payload)

        # Zero-Knowledge Encryption Storage
        raw_data = f"URI:{uri} | Cat:{category if category else 'NONE'} | RawPayload:{raw_safe_payload}"
        key = self._generate_key(user_secret)
        encrypted_data = self._cipher_payload(raw_data, key)

        conn = sqlite3.connect(self.vault_filename)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO standard_registry (resource_id, uri, category_header, compliance_status, encrypted_payload)
            VALUES (?, ?, ?, ?, ?)
        ''', (resource_id, uri, category if category else "UNCATEGORIZED", compliance_status, encrypted_data))
        conn.commit()
        conn.close()

        if compliance_status == "UNTRUSTED_DANGER_ZONE":
            return self._execute_security_shield(uri)
        return True

    def _execute_security_shield(self, uri: str) -> bool:
        """The Official Security Shield mandated by op's standard"""
        print(f"\n\033[95m[Httpsh Security Protocol by op]\033[96m")
        print(f"Target URI: {uri}")
        print("-" * 60)
        print(f"🛡️ [Security Guarantee]: You are protected even from me in a terrifyingly absolute way! 👻🔒{self.reset_code}")
        print("-" * 60)

        print(f"\n\033[41m\033[97m🚨 [Standard Alert]: Initiating 10-step security deterrence sequence...\033[0m")
        for i in range(1, 11):
            print(f"Standard Warning ({i}/10): Entering an unverified/hazardous protocol space!")
            time.sleep(0.01)

        print("\n" + "=" * 65)
        print("📜 [Httpsh Protocol Disclaimer - Authored by op]:")
        print("I acknowledge the protocol's warning. I assume absolute, sovereign responsibility.")
        print("I promise never to hold the standard creator (op) liable for my actions.")
        print("=" * 65)

        agreement = input("Type 'yes' to accept standard liability and proceed: ").strip().lower()
        return agreement in ["yes", "y", "نعم"]

    def export_to_text_file(self, resource_id: str, output_filepath: str = None) -> str:
        """
        Exports stored resource as a pure, raw, non-interactive plain text file (.txt or .httpsh)
        compatible with external browsers or editors.
        """
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

"""
================================================================================
STANDARD SPECIFICATION: Httpsh Protocol Core Engine (v1.0 - Pure Text & Code Edition)
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
    The Official Reference Engine for Httpsh Protocol Standard (v1.0).
    Designed for local-first, zero-knowledge, low-resource environments (<= 2GB RAM).
    Architected by op.
    """
    def __init__(self, vault_filename="httpsh_sovereign_vault.db", hardware_ram_gb: float = 2.0):
        self.vault_filename = vault_filename
        self.ram_gb = hardware_ram_gb
        self._enforce_resource_profile()
        self._init_sovereign_vault()
        
        # Windows-like Theme & Background Registry (Default: Clean White bg / Black text)
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
        if self.ram_gb <= 2
