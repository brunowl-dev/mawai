const form = document.getElementById('itemForm');
const itemsList = document.getElementById('items');

const loadItems = async () => {
  try {
    const response = await fetch('/api/tracks');
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
    const response = await fetch('/api/tracks', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });

    if (response.ok) {
      form.reset();
      loadItems();
    }
  } catch (error) {
    console.error('Erro ao salvar item:', error);
  }
});

loadItems();
