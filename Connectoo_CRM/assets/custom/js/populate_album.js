var myAlbum = {};

myAlbum.albumArr = JSON.parse(localStorage.getItem('imgData'));

myAlbum.populate=function () {
    var box = $('.cbp-wrapper');
    box.html('<div class="cbp-item web-design graphic print motion"><a href="#" class="cbp-caption"><div class="cbp-caption-defaultWrap"><img src="http://kingofwallpapers.com/picture/picture-008.jpg"></div><div class="cbp-caption-activeWrap"><div class="cbp-l-caption-alignLeft"><div class="cbp-l-caption-body"><div class="cbp-l-caption-title"></div><div class="cbp-l-caption-desc"></div><button type="button" class="btn btn-circle green btn-sm album">Add to Album</button></div></div></div></a></div>')

        // var holder = $('<div/>', {'class': "cbp-item web-design graphic print motion"});

        // var content = $('<div/>', {'class': "cbp-item-wrapper"}).appendTo(holder);
        // $('<a/>', {'class': "cbp-caption", 'href': "#"}).append(        
        //     $('<div/>', {'class': "cbp-caption-defaultWrap"}).append(
        //         $('<img/>', {'src': 'http://kingofwallpapers.com/picture/picture-008.jpg'})// myAlbum.albumArr[i]})
        //     )
        // ).appendTo(content);
        
        // $('<div/>', {'class': "cbp-caption-activeWrap"}).append(
        //     $('<div/>', {'class': "cbp-caption-alignleft"}).append(
        //         $('<div/>', {'class': "cbp-l-caption-body"}).html(
        //             '<div class="cbp-l-caption-title"></div>'
        //         )
        //     )
        // ).appendTo(content)

        // content.appendTo(box)
};

$(document).ready(function() {
    alert('hey');
    myAlbum.populate();
});