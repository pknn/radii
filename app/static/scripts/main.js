$('document').ready(function () {
    console.log('Hi');
})

let numberOfEvent = $('.grid .services').length;
let limitEvent = 9;
$(".grid .services:gt(" + (limitEvent-1) + ")").hide();
let totalPages = Math.round(numberOfEvent/limitEvent);
let currentPage = $(".pagination p").text();

$(".pagination li.next").on("click", function() {    
    if(currentPage == totalPages || totalPages == 0){                
        return false;        
    } else {        
        currentPage++;
        $('.pagination li').removeClass("active")
        $('.grid .services').hide();
        change_page();
    }
})

$(".pagination li.previous").on("click", function() {
    if(currentPage == 1){
        return false;
    } else {
        currentPage--;
        $('.pagination li').removeClass("active")
        $('.grid .services').hide();
        change_page();
    }
})

function change_page(){
    let grandTotal = limitEvent * currentPage        
    for (let i=grandTotal-limitEvent; i<grandTotal; i++){
        $(".grid .services:eq(" + (i) + ")").show();
    }        
    $(".pagination li.page-current").addClass("active");
    $(".pagination p").text(currentPage);
}
