let formCounter = 1;

function agregarFormulario() {
  // Clona el formulario original
  const formularioOriginal = document.getElementById('formulario-original');
  const nuevoFormulario = formularioOriginal.cloneNode(true);

  // Actualiza los atributos de los campos clonados para que tengan nombres únicos
  const inputNumeroContenido = nuevoFormulario.querySelector('[name="nombre-contenido"]');
  const inputContenido = nuevoFormulario.querySelector('[name="horas-doncencia"]');
  const selectUnidad = nuevoFormulario.querySelector('[name="horas-practica"]');

  console.log("inputNumeroContenido:", inputNumeroContenido);
  console.log("inputContenido:", inputContenido);
  console.log("selectUnidad:", selectUnidad);

  //inputNumeroContenido.name = `nombre-contenido_${formCounter}`;
  //inputContenido.name = `horas-doncencia_${formCounter}`;
  //selectUnidad.name = `horas-practica_${formCounter}`;

  // Incrementa el contador para el siguiente formulario
  formCounter++;

  // Agrega el nuevo formulario como una nueva fila al contenedor de filas
  const formulariosFilasContainer = document.getElementById('formularios-filas');
  formulariosFilasContainer.appendChild(nuevoFormulario);
}
