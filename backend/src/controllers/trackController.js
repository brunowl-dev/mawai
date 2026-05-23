const trackService = require('../services/dbService');

const listTracks = async (req, res) => {
  try {
    const items = await trackService.getAllItems();
    res.json(items);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Erro ao buscar itens' });
  }
};

const createTrack = async (req, res) => {
  const { title, type, category, note } = req.body;

  if (!title || !type) {
    return res.status(400).json({ error: 'Título e tipo são obrigatórios' });
  }

  try {
    const result = await trackService.createItem({ title, type, category, note });
    res.status(201).json({ id: result.id });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Erro ao criar item' });
  }
};

module.exports = {
  listTracks,
  createTrack,
};
