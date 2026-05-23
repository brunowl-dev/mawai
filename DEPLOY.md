# 🚀 Guia de Publicação com Dados Compartilhados

## 🎯 Arquitetura

Para que você e sua namorada vejam os mesmos dados em tempo real:

```
Frontend (GitHub Pages)      Backend (Render)
   ↓                              ↑
https://brunowl-dev.github.io/mawai/ ←→ https://mawai-backend.onrender.com
                                ↓
                            SQLite Database
```

## 📋 Passo 1: Preparar Repositório Git

```bash
# Certificar que tudo está commitado
git add .
git commit -m "Setup for GitHub Pages + Render backend"
git push origin main
```

## 🌐 Passo 2: Deploy do Backend no Render

### Opção A: Deploy Automático (Recomendado)

1. Acesse [render.com](https://render.com)
2. Clique em **New +** → **Web Service**
3. Conecte seu repositório GitHub
4. Selecione `mawai`
5. Configure:
   - **Name:** `mawai-backend`
   - **Environment:** `Node`
   - **Build Command:** `npm install`
   - **Start Command:** `npm start`
   - **Plan:** Free (suficiente para começar)
6. Clique em **Create Web Service**

Render vai gerar uma URL como: `https://mawai-backend.onrender.com`

### Opção B: Deploy Manual

Se preferir usar CLI do Render:

```bash
# Instalar Render CLI (opcional)
npm install -g render-deploy

# Fazer deploy
render deploy
```

## 🔗 Passo 3: Atualizar URL da API

Após o Render gerar a URL, atualize em `frontend/js/app.js`:

```javascript
const API_URL = process.env.NODE_ENV === 'production' 
  ? 'https://mawai-backend.onrender.com/api/tracks'  // ← Sua URL do Render
  : '/api/tracks';
```

**OU** defina como variável de ambiente:

```bash
export REACT_APP_API_URL=https://mawai-backend.onrender.com/api/tracks
```

## 📚 Passo 4: Deploy do Frontend no GitHub Pages

1. Vá para **Settings** do repositório
2. **Pages** → 
   - Source: "Deploy from a branch"
   - Branch: `gh-pages`
3. Clique em **Save**

```bash
npm install
npm run deploy
```

A aplicação estará em: **`https://brunowl-dev.github.io/mawai/`**

## ✅ Testando

1. **Abra em dois navegadores/abas:**
   - https://brunowl-dev.github.io/mawai/
   - https://brunowl-dev.github.io/mawai/ (em outro navegador ou incógnito)

2. **Adicione um item em uma aba**
3. **Recarregue a outra aba** (Ctrl+R)
4. O item deve aparecer! ✨

Se não aparecer:
- Verifique o console (F12) para erros
- Certifique-se que a URL do Render está correta
- Teste se o backend está respondendo: `curl https://mawai-backend.onrender.com/api/tracks`

## 📱 Compartilhando com Sua Namorada

Simplesmente envie o link:
```
https://brunowl-dev.github.io/mawai/
```

Ambos verão os mesmos itens! Os dados estão no banco SQLite do Render.

## 🔒 Sobre Segurança

⚠️ **Por enquanto é público!** Qualquer pessoa que souber o link pode:
- Ver todos os itens
- Adicionar itens
- Potencialmente deletar itens

Para adicionar segurança no futuro:
- Autenticação com usuário/senha
- Chaves de API
- JWT tokens

## 🆚 GitHub Pages vs Render

| Feature | GitHub Pages | Render |
|---------|---|---|
| **Frontend Estático** | ✅ Grátis | ❌ Pago |
| **Backend Node.js** | ❌ Não suporta | ✅ Grátis (free tier) |
| **Banco de Dados** | ❌ Não | ✅ SQLite incluído |
| **Dados Compartilhados** | ❌ Não | ✅ Sim |

## 💡 Alternativas

Se o Render não funcionar bem:

### Firebase/Firestore (Recomendado para começar)
- Banco de dados em tempo real
- Autenticação incluída
- 1GB de armazenamento grátis

### Supabase (PostgreSQL)
- Open-source
- Database PostgreSQL
- Autenticação
- Grátis

### Vercel + API Routes
- Deploy o backend em Vercel
- Frontend também em Vercel
- Grátis

## 🚀 Próximos Passos

1. Fazer deploy do backend no Render
2. Copiar a URL gerada pelo Render
3. Atualizar `app.js` com essa URL
4. Fazer deploy do frontend no GitHub Pages
5. Testar em dois navegadores

Qualquer dúvida, cheque os logs:
- **Backend:** Dashboard do Render → Logs
- **Frontend:** DevTools → Console (F12)

