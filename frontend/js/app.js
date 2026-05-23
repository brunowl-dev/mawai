const form = document.getElementById('itemForm');
const itemsList = document.getElementById('items');

// URL da API (muda conforme ambiente)
const API_URL = process.env.NODE_ENV === 'production' 
  ? 'https://mawai-backend.onrender.com/api/tracks'
  : '/api/tracks';

const loadItems = async () => {
  try {
    const response = await fetch(API_URL);
    const data = await response.json();
    itemsList.innerHTML = data.map(item => `
      <li>
        <strong>${item.title}</strong> <span>(${item.type})</span>
        <p>${item.category || ''}</p>
        <p>${item.note || ''}</p>
      </li>
    `).join('');
  } catch (error) {
    console.error('Erro ao carregar itens:', error);
    itemsList.innerHTML = '<li>Erro ao conectar ao servidor. Verifique sua conexão.</li>';
  }
};

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const payload = {
    title: document.getElementById('title').value.trim(),
    type: document.getElementById('type').value,
    category: document.getElementById('category').value.trim(),
    note: document.getElementById('note').value.trim(),
  };

  try {
    const response = await fetch(API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });

    if (response.ok) {
      form.reset();
      loadItems();
    } else {
      alert('Erro ao salvar item. Tente novamente.');
    }
  } catch (error) {
    console.error('Erro ao salvar item:', error);
    alert('Erro ao conectar ao servidor. Verifique sua conexão.');
  }
});

loadItems();
