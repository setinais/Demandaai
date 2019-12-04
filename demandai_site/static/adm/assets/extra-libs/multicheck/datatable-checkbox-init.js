
// function checkbox(model){
//     $('#mainCheckbox'+model).multicheck($('.listCheckbox'+model));
// }

function setChecks(codigo) {
    $('[name='+codigo+']').prop('checked', true);
}
$(function() {
    //multicheckbox check for static table no padding
    $('#mainCheckbox-prospeccao').multicheck($('.listCheckbox-prospeccao'));
    $('#mainCheckbox-service').multicheck($('.listCheckbox-service'));
    $('#mainCheckbox-laboratory').multicheck($('.listCheckbox-laboratory'));
    $('#mainCheckbox-equipament').multicheck($('.listCheckbox-equipament'));
    $('#mainCheckbox-profile').multicheck($('.listCheckbox-profile'));
    $('#mainCheckbox-institution').multicheck($('.listCheckbox-institution'));
    $('#mainCheckbox-permission').multicheck($('.listCheckbox-permission'));

    //multicheckbox check for static table with padding
    // $('#mainCheckbox1').multicheck($('.listCheckbox1'));

    /*var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-36251023-1']);
    _gaq.push(['_setDomainName', 'jqueryscript.net']);
    _gaq.push(['_trackPageview']);

    (function() {
        var ga = document.createElement('script');
        ga.type = 'text/javascript';
        ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(ga, s);
    })();*/



});