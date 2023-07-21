// scripts.js
let formCounter = 1;
function agregarFormulario() {
  // Clona el formulario original
  const formularioOriginal = document.querySelector('#formularios-container form');
  const nuevoFormulario = formularioOriginal.cloneNode(true);

  // Actualiza los atributos de los campos clonados para que tengan nombres únicos
  const inputNumeroContenido = nuevoFormulario.querySelector('[name="cedula"]');
  const inputContenido = nuevoFormulario.querySelector('[name="nombres"]');
  const selectUnidad = nuevoFormulario.querySelector('[name="unidad"]');

  inputNumeroContenido.name = `cedula_${formCounter}`;
  inputContenido.name = `nombres_${formCounter}`;
  selectUnidad.name = `unidad_${formCounter}`;

  // Incrementa el contador para el siguiente formulario
  formCounter++;

  // Agrega el nuevo formulario al contenedor
  const formulariosContainer = document.getElementById('formularios-container');
  formulariosContainer.appendChild(nuevoFormulario);
}
