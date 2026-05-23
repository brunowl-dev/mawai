# Mawai

Ferramenta de tracklist para uso individual e duplo. Organize filmes, séries, jogos e músicas que você quer acompanhar.

## 🚀 Acesso Online

A aplicação está disponível em GitHub Pages:  
**[https://brunowl-dev.github.io/mawai/](https://brunowl-dev.github.io/mawai/)**

Você e sua namorada podem acessar o mesmo link e os dados são **compartilhados em tempo real**! 🎉

## 💾 Dados Compartilhados

Os itens que vocês adicionam são salvos em um banco de dados SQLite no servidor Render. Isso significa:
- ✅ Dados compartilhados em tempo real entre vocês
- ✅ Sincronização automática
- ✅ Funciona em qualquer dispositivo/navegador
- ✅ Sem limite de sincronização

## 🛠️ Para Desenvolvimento Local

### Requisitos
- Node.js 18+
- npm ou yarn

### Instalação

```bash
# Instalar dependências
npm install

# Executar em desenvolvimento (com backend local)
npm run dev

# Abrir em http://localhost:3000
```

### Build & Deploy

Para fazer deploy:

1. **Backend** (Render):
   ```bash
   git push origin main
   # Render faz deploy automático via render.yaml
   ```

2. **Frontend** (GitHub Pages):
   ```bash
   npm run deploy
   ```

Veja [DEPLOY.md](./DEPLOY.md) para instruções detalhadas.

## 📁 Estrutura do Projeto

```
mawai/
├── frontend/          # Aplicação estática (HTML, CSS, JS)
│   ├── index.html
│   ├── css/style.css
│   └── js/app.js     # Faz chamadas para API
├── backend/          # Backend Node.js (API)
│   ├── server.js
│   ├── database.js
│   └── src/
│       ├── controllers/
│       ├── routes/
│       └── services/
├── database/         # SQLite (Dados Compartilhados)
├── render.yaml       # Config para deploy no Render
└── DEPLOY.md         # Guia de deployment
```

## 🎯 Recursos

- ✏️ Adicionar itens (filmes, séries, jogos, músicas)
- 📝 Adicionar categorias e notas
- 📋 Visualizar lista de itens
- 🔄 Dados sincronizados em tempo real com sua namorada
- 💾 Persistência em banco de dados

## 🤝 Compartilhando

Simples: envie o link para sua namorada!

```
https://brunowl-dev.github.io/mawai/
```

Ambos verão os mesmos dados, adições e atualizações em tempo real.

## 📚 Documentação

- [DEPLOY.md](./DEPLOY.md) - Guia completo de deployment
- [requisitos.txt](./requisitos.txt) - Dependências Python (scripts auxiliares)


