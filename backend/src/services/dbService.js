const { db, initialize } = require('../../database');

const getAllItems = () => {
  return new Promise((resolve, reject) => {
    db.all('SELECT * FROM items ORDER BY created_at DESC', (err, rows) => {
      if (err) return reject(err);
      resolve(rows);
    });
  });
};

const createItem = ({ title, type, category, note }) => {
  return new Promise((resolve, reject) => {
    const stmt = db.prepare(
      'INSERT INTO items (title, type, category, note) VALUES (?, ?, ?, ?)',
    );
    stmt.run(title, type, category, note, function (err) {
      if (err) return reject(err);
      resolve({ id: this.lastID });
    });
    stmt.finalize();
  });
};

module.exports = {
  initialize,
  getAllItems,
  createItem,
};
