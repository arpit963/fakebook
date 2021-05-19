$(document).ready(function(){
    console.log('Hello from the base')
})

$(document).ready(function(){
    $('#modal-btn').click(function(){
        $('.ui.modal')
        .modal('show');
    })
    $('.ui.dropdown').dropdown()
})