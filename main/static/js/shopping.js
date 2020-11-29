const itemsEachPage = 6;

async function getProducts(page, nItems) {
    let url = `/products?page=${page}&items_per_page=${nItems}`
    let response = await fetch(url);
    let jsonResponse = await response.json();
    totalItems = jsonResponse.total_items;
    items = jsonResponse.items;
    if (response.status == 200) {
        cards = $('#sec-shopping .card');
        for (let i = 0; i < cards.length; ++i) {
            cards[i].querySelector('a').href = items[i].url;                            
            cards[i].querySelector('.card-img-top').src = items[i].thumbnail;
            cards[i].querySelector('.price').innerHTML = `$${items[i].price}`;
            cards[i].querySelector('.fa-star').innerHTML = ` ${items[i].rating}`;
            cards[i].querySelector('.fa-comment-dots').innerHTML = ` ${items[i].total_reviews}`;
            cards[i].querySelector('.card-text').innerHTML = `${items[i].title}`;
            
        }
    } else {
        console.log(response.message);
    }
}

$(document).ready(function () {
    getProducts(1, itemsEachPage);
});

$('.pagination a').on('click', function() {
    $('.pagination a').removeClass('pagination-active');
    $(this).addClass('pagination-active');
    let page = parseInt($(this).text());
    console.log(page)
    getProducts(page, itemsEachPage);
})