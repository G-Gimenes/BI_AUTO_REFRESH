# 📊🔄 BI_AUTO_REFRESH

Automatizador de atualização de datasets no **Power BI** via API, utilizando autenticação no **Azure Active Directory** e disparo de refresh automático.

---

## 📌 Objetivo

Este projeto tem como finalidade automatizar o processo de atualização de datasets no Power BI, evitando a necessidade de disparos manuais e/ou a limitação de quantidade de disparos agendados permitidos por licença do Power BI, garantindo que os relatórios estejam sempre atualizados.

---

## ⚙️ Configuração

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seuusuario/BI_AUTO_REFRESH.git
cd BI_AUTO_REFRESH
```

### 2️⃣ Instalar as dependências

```bash
pip install -r requirements.txt
```

### 3️⃣ Configurar credenciais

1. Copie o arquivo de exemplo:

```bash
cp config/settings_example.json config/settings.json
```

2. Preencha o arquivo `config/settings.json` com seus dados reais:

```json
{
  "TENANT_ID": "seu-tenant-id",
  "CLIENT_ID": "seu-client-id",
  "CLIENT_SECRET": "seu-client-secret",
  "USERNAME": "usuario@dominio.com",
  "PASSWORD": "sua-senha",
  "GROUP_ID": "seu-group-id",
  "DATASET_ID": "seu-dataset-id"
}
```

---

## 📜 Exemplo de saída no console

```text
=== 🏁 INÍCIO DO PROCESSO DE ATUALIZAÇÃO DO DATASET POWER BI 🏁 ===
[AUTH] Iniciando autenticação no Azure Active Directory...
[AUTH] Autenticação realizada com sucesso. Token de acesso obtido.
[REFRESH] Enviando solicitação de atualização do dataset...
[REFRESH] Código de resposta HTTP: 202
[REFRESH] Solicitação aceita com sucesso. Atualização do dataset iniciada.
=== 🏁 FIM DO PROCESSO DE ATUALIZAÇÃO DO DATASET POWER BI 🏁 ===
```


---

## 🧾 Licença

Este projeto está licenciado sob a **MIT License** — uso livre para fins pessoais e comerciais, desde que os créditos sejam mantidos.

Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👤 Créditos

Desenvolvido por **Gustavo Gimenes**  
Automação de refresh de datasets Power BI via API e Azure Active Directory.

Se este projeto te ajudou, mantenha os créditos 🙂
