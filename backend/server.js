const express = require('express');
const path = require('path');
const cors = require('cors');
const { initialize } = require('./database');
const trackRoutes = require('./src/routes/trackRoutes');

const app = express();
const port = process.env.PORT || 3000;

// CORS configuration para aceitar requisições do GitHub Pages
const corsOptions = {
  origin: [
    'http://localhost:3000',
    'http://localhost:5000',
    'https://brunowl-dev.github.io',
  ],
  optionsSuccessStatus: 200,
};

app.use(cors(corsOptions));
app.use(express.json());

// Se não estiver em produção, servir arquivos estáticos também
if (process.env.NODE_ENV !== 'production') {
  app.use(express.static(path.join(__dirname, '..', 'frontend')));
  app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '..', 'frontend', 'index.html'));
  });
}

app.use('/api/tracks', trackRoutes);

initialize();

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
