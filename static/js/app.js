// JS mínimo: só cola entre HTMX e a página. Regras de negócio ficam SEMPRE no backend.
document.addEventListener('DOMContentLoaded', () => {
  const body = document.body;
  // Formulário com erro volta do backend como 422; sem isto o HTMX ignoraria a resposta.
  body.addEventListener('htmx:beforeSwap', e => {
    if (e.detail.xhr.status === 422) { e.detail.shouldSwap = true; e.detail.isError = false; }
  });
  // Evento disparado pelo backend via header HX-Trigger para fechar o modal.
  body.addEventListener('modal-fechar', () => { document.getElementById('modal-root').innerHTML = ''; });
  document.addEventListener('keydown', e => { if (e.key === 'Escape') htmx.trigger(body, 'modal-fechar'); });
  // Toast: HX-Trigger {"toast": {"msg": "Salvo"}}
  body.addEventListener('toast', e => {
    const t = document.createElement('div'); t.className = 'toast'; t.textContent = e.detail.msg || e.detail.value;
    document.getElementById('toasts').append(t); setTimeout(() => t.remove(), 4000);
  });
});
