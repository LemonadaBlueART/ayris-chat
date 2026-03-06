"""from openai import OpenAI
import os
import json

class AyrisAI:
    MEMORIA_FILE = "/home/asm/Documentos/Ayris-main/Ayris/Source/Memory/memoria_ayris.json"

    def __init__(self, provedor="ollama"):
        self.provedor = provedor.lower()
        self.client = self._configurar_cliente()

    def _configurar_cliente(self):
        if self.provedor == "groq":
            return OpenAI(
                base_url="https://api.groq.com/openai/v1",
                api_key="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" 
            )

    def _get_model_name(self):
        modelos = {
            #"groq": "llama-3.1-8b-instant",
            "groq": "llama-3.3-70b-versatile",
        }
        return modelos.get(self.provedor)

    def carregar_historico(self):
        if os.path.exists(self.MEMORIA_FILE):
            try:
                with open(self.MEMORIA_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except: return []
        return []

    def salvar_historico(self, historico):
        with open(self.MEMORIA_FILE, 'w', encoding='utf-8') as f:
            json.dump(historico, f, indent=4, ensure_ascii=False)

    def Prompt(self, system_prompt, user_input):
        historico = self.carregar_historico()

        if not historico or historico[0]["role"] != "system":
            historico.insert(0, {"role": "system", "content": system_prompt})
        else:
            historico[0]["content"] = system_prompt

        historico.append({"role": "user", "content": user_input})

        if len(historico) > 32: 
            historico = [historico[0]] + historico[-30:] 
        
        mensagens = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]

        try:
            completion = self.client.chat.completions.create(
                model=self._get_model_name(),
                messages=historico,
                temperature=1.0,
                max_tokens=1024,
            )
            
            resposta = completion.choices[0].message.content
            historico.append({"role": "assistant", "content": resposta})


            self.salvar_historico(historico)
            return resposta

        except Exception as e:
            return f"Erro: {e}"
"""

"""import os
import json
from llama_cpp import Llama

class AyrisAI:
    MEMORIA_FILE = "/home/asm/Documentos/Ayris-main/Ayris/Source/Memory/memoria_ayris.json"

    def __init__(self, model_path="/home/asm/Documentos/Ayris-main/Ayris/Source/Models/Llama-3.2-1B-Instruct-UD-IQ1_M.gguf"):
        self.model_path = model_path
        # Inicializando o modelo local usando llama_cpp
        self.llm = Llama(
            model_path=self.model_path,
            n_ctx=4096,
            n_threads=4  # ideal para i5-6500
        )

    def carregar_historico(self):
        #Carrega o histórico de interações da IA.
        if os.path.exists(self.MEMORIA_FILE):
            try:
                with open(self.MEMORIA_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []

    def salvar_historico(self, historico):
        #Salva o histórico de interações da IA.
        with open(self.MEMORIA_FILE, 'w', encoding='utf-8') as f:
            json.dump(historico, f, indent=4, ensure_ascii=False)

    def Prompt(self, system_prompt, user_input):
        #Gera uma resposta da IA com base no histórico e entrada do usuário.
        # Carregar histórico da memória
        historico = self.carregar_historico()

        # Verificar se o histórico precisa ser inicializado com a personalidade
        if not historico or historico[0]["role"] != "system":
            historico.insert(0, {"role": "system", "content": system_prompt})
        else:
            historico[0]["content"] = system_prompt

        # Adicionar a entrada do usuário ao histórico
        historico.append({"role": "user", "content": user_input})

        # Manter o histórico dentro do limite de 8 interações
        if len(historico) > 4:
            historico = [historico[0]] + historico[-3:]

        try:
            # Chama o modelo local para gerar a resposta
            response = self.llm.create_chat_completion(
                messages=historico,
                temperature=1.0,
                max_tokens=512
            )

            # Extrai a resposta e adiciona ao histórico
            resposta = response["choices"][0]["message"]["content"]
            historico.append({"role": "assistant", "content": resposta})

            # Salvar o histórico após a interação
            self.salvar_historico(historico)
            return resposta

        except Exception as e:
            return f"Erro: {e}"

            """


"""import os
import json
from llama_cpp import Llama

class AyrisAI:
    def __init__(self, model_path="/home/asm/Documentos/Ayris-main/Ayris/Source/Models/Llama-3.2-1B-Instruct-UD-IQ1_M.gguf"):
        self.model_path = model_path
        # Inicializando o modelo local usando llama_cpp
        self.llm = Llama(
            model_path=self.model_path,
            n_ctx=4096,
            n_threads=4  # ideal para i5-6500
        )

    def Prompt(self, system_prompt, user_input):
        # Gera uma resposta da IA com base na entrada do usuário, sem histórico.
        
        try:
            # Chama o modelo local para gerar a resposta
            response = self.llm.create_chat_completion(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                temperature=1.0,
                max_tokens=512
            )

            # Extrai a resposta
            resposta = response["choices"][0]["message"]["content"]
            return resposta

        except Exception as e:
            return f"Erro: {e}"

"""

import os
import json
from llama_cpp import Llama

class AyrisAI:
    MEMORIA_FILE = "/home/asm/Documentos/Ayris-main/Ayris/Source/Memory/memoria_ayris.json"

    def __init__(self, model_path="/home/asm/Documentos/Ayris-main/Ayris/Source/Models/Qwen2.5-Coder-0.5B-Instruct-abliterated-Q5_K_M.gguf"):
        self.model_path = model_path
        
        # ==========================================
        # 1 e 2. CONTROLE DE HARDWARE (RAM, VRAM e THREADS)
        # ==========================================
        print("Carregando o modelo de linguagem...")
        self.llm = Llama(
            model_path=self.model_path,
            
            # --- Controle de VRAM (Placa de Vídeo) ---
            n_gpu_layers=0, 
            
            # --- Controle de RAM (Memória do Sistema) ---
            # n_ctx: 50000 é bem alto e consumirá bastante RAM.
            n_ctx=10000,
            
            # --- Controle de Threads (Processador) ---
            n_threads=2,
            
            # --- Controle de Threads Iniciais (Processador)
            n_threads_batch=2,
    
            # 4. n_batch ajuda no processamento inicial do texto
            n_batch=3000,    
            
            # verbose=False desativa aquele monte de texto técnico no terminal ao carregar
            verbose=False 
        )

    def carregar_historico(self):
        """Carrega o histórico de interações da IA."""
        if os.path.exists(self.MEMORIA_FILE):
            try:
                with open(self.MEMORIA_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except: 
                return []
        return []

    def salvar_historico(self, historico):
        """Salva o histórico de interações da IA no arquivo JSON."""
        # Cria o diretório se não existir
        os.makedirs(os.path.dirname(self.MEMORIA_FILE), exist_ok=True)
        with open(self.MEMORIA_FILE, 'w', encoding='utf-8') as f:
            json.dump(historico, f, indent=4, ensure_ascii=False)

    def Prompt(self, system_prompt, user_input):
        """Gera uma resposta da IA com base no histórico e entrada do usuário."""
        historico = self.carregar_historico()

        # Verificar se o histórico precisa ser inicializado com a personalidade
        if not historico or historico[0].get("role") != "system":
            historico.insert(0, {"role": "system", "content": system_prompt})
        else:
            # Atualiza a personalidade caso tenha mudado no código principal
            historico[0]["content"] = system_prompt

        # Adicionar a entrada do usuário ao histórico
        historico.append({"role": "user", "content": user_input})

        # Manter o histórico dentro do limite (ex: 32 interações) para não estourar o contexto
        if len(historico) > 9: 
            # Mantém o prompt de sistema [0] e pega as últimas 30 mensagens
            historico = [historico[0]] + historico[-8:] 

        try:
            print("Gerando resposta...\n")
            
            # ==========================================
            # 4. CONTROLE DE PARÂMETROS DE GERAÇÃO
            # ==========================================
            response = self.llm.create_chat_completion(
                messages=historico,
                
                # Temperature: Controla a criatividade.
                temperature=0.7,
                
                # Max Tokens: Limite máximo de palavras/pedacinhos.
                max_tokens=2000,
                
                # Top P: Outra forma de controlar a criatividade.
                top_p=1.0,
                
                # Repeat Penalty: Pune o modelo se ele começar a repetir a mesma palavra.
                repeat_penalty=1.15
            )

            # Extrai a resposta e adiciona ao histórico
            resposta = response["choices"][0]["message"]["content"]
            historico.append({"role": "assistant", "content": resposta})

            # Salvar o histórico após a interação
            self.salvar_historico(historico)
            
            return resposta

        except Exception as e:
            return f"Erro durante a geração: {e}"