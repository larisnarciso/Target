var listaUl = document.querySelector('ul.custom-controls');
var listaLi = listaUl.querySelectorAll('li');
var listaQuestoes = document.querySelectorAll('.lista-questoes li');

listaLi.forEach((imagem, index) => {
  imagem.addEventListener('click', function () {
    mostrarQuestao(index);
    atualizarClasseAtiva(imagem);
  });
});

function atualizarClasseAtiva(botaoSelecionado) {
  listaLi.forEach((botao) => {
    botao.classList.remove('active');
  });
  botaoSelecionado.classList.add('active');
}

function mostrarQuestao(index) {
  listaQuestoes.forEach((questao, i) => {
    if (i === index) questao.style.display = 'block';
    else questao.style.display = 'none';
  });
}
