import 'normalize_css';
import 'main_css';
import 'slides_js';
import '../../modules/add_slides_itemhover';

$(function () {
    function get_query(){
        let search = $('#search-input').val();
        let level = $('.classes-select option:selected').val();
        let query = {}
        if (search){ query['search'] = search}
        if (level) { query['level'] = level}
        return $.param(query)
    }
    function fresh_page(){
        let w_location = window.location;
        let query = get_query()
        w_location.href = w_location.origin + w_location.pathname + '?' + query
    }
    $('.classes-select').change(function () {
        fresh_page()
    });

    $('#search-button').click(function(){
        fresh_page()
    })
    $(document).keypress(function(e) {
        if(e.which == 13) {
            fresh_page()
        }
    });
});
