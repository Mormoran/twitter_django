var element = document.getElementById('choose-user')

// Attach a function to the change event
// This function will be called when the select value changes
element.onchange = function () {
  window.location.assign('/graphs/show/?username=' + element.value)
}