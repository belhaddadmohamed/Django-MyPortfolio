

$(document).on('click', '.project_card', function(){
    let this_val = $(this)
    let id = this_val.attr('data-id')


    console.log(id)
    $.ajax({
        url: '/single-project',
        data: {'id': id},
        dataType: 'json',
        success: function(resp){
            // <!-- <body id="page-top" class="modal-open" style="overflow: hidden; padding-right: 19px;"> -->
            $('#portfolio-description').html(resp.project_details)
            $('#backdrop').addClass("modal-backdrop fade show")
        },
    })
})



$(document).on('click', '.close_window', function(){
    $('#portfolio-description').html(``)
    $('#backdrop').removeClass("modal-backdrop show")
})



$(document).on('submit', '#contactForm', function(e){
    e.preventDefault();

    $.ajax({
        url: $(this).attr('action'),
        method: $(this).attr('method'),
        data: $(this).serialize(),
        dataType: 'json',
        success: function(resp){
            if(resp.bool){
                // Hide the submit button
                $('#submitButton').hide()
                console.log('Form submitted')
                
                // Show the success message
                $('#submitSuccessMessage').removeClass('d-none')
            }
        },
    })
    
})