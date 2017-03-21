var myAlbum = {};

myAlbum.albumArr = JSON.parse(localStorage.getItem('imgData'));

myAlbum.populate=function () {
    var box = $('#cn-pageContent');
    
    if (!myAlbum.albumArr) {
            box.append('<h1>No photos added</h1></br><p>Please select photos you want to print</p>')
            row = $('<div/>', {'class': "row"});
        }
        else {
            var row = $('<div/>', {'class': "row"});

            for (var i = 0; i < myAlbum.albumArr.length; i++) {        
                if (i % 4 == 0 && i != 0) {
                    box.append(row)
                    row = $('<div/>', {'class': "row"});
                }
                url = 'url("'+ myAlbum.albumArr[i] +'")'
                var image = $('<div/>', {'class': "col-md-3 col-lg-3"}).append(
                                $('<div/>').css({
                                    'width':'100%',
                                    'height':'200px',
                                    'background-image':url,
                                    'background-position':'center',
                                    'background-size':'cover'})
                                // .append($('<img/>', {'src': myAlbum.albumArr[i]}).css({'width': '100%', 'overflow':'hidden'}))
                            ).appendTo(row);
                }
                box.append(row);
        }
        $('.row').css('margin-bottom', '25px');
    };

myAlbum.deleteAlbum = function () {
    var sure = confirm('Are you sure you want to delete your album?');
    if (sure) {
        localStorage.removeItem('imgData');
    }
}

$(document).ready(function() {
    myAlbum.populate();
    $('#delete-album').bind('click', myAlbum.deleteAlbum);
});