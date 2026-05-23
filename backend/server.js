const express = require('express');
const path = require('path');
const { initialize } = require('./database');
const trackRoutes = require('./src/routes/trackRoutes');

const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());
app.use(express.static(path.join(__dirname, '..', 'frontend')));

app.use('/api/tracks', trackRoutes);

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '..', 'frontend', 'index.html'));
});

initialize();

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
