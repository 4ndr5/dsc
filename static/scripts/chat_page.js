document.addEventListener('DOMContentLoaded', () => {
    
       // Destroy the living hell out of sidebar
       document.querySelector('#show-sidebar-button').onclick = () => {
        document.querySelector('#sidebar').classList.toggle('view-sidebar');
    };
    
    //make 'enter' key submit msg
    let msg = document.querySelector('#user_message');
    msg.addEventListener('keyup', event => {
        if (event.keyCode === 13) {
            document.querySelector('#send_message').click();
        };
    });
})