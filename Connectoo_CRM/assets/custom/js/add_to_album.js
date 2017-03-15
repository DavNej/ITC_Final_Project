var myAlbum = myAlbum || {};
	myAlbum.cardArr = JSON.parse(localStorage.getItem('imgData'));
myAlbum.createImg=function () {
    for (var i=0; i<myAlbum.cardArr.length; i++){
        console.log(myAlbum.cardArr[i]);
        $('body').append(
        $('<div/>', {'class': "cbp-item web-design graphic print motion"}).append(
            // $('<div <a href =\"#" class="cbp-caption cbp-singlePageInline" data-title="World Clock Widget<br>by Paul Flavius Nechita" rel="nofollow"> </a> </div>)}.append(

            $('<div/>', {'class': 'cbp-caption-defaultWrap '}).append(
                $('<img/>').attr('src', myAlbum.cardArr[i])
            )
        )
    )

    }
};

myAlbum.createImg();