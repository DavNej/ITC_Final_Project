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
                var image = $('<div/>', {'class': "col-md-3 col-lg-3"}).append(
                                $('<div/>').css({'width':'100%','height':'100%','background-color':'black'}).append(
                                    $('<img/>', {'src': myAlbum.albumArr[i]}).css({'width': '100%', 'overflow':'hidden'})
                                )
                            ).appendTo(row);
                }
                box.append(row)
        }
    };

$(document).ready(function() {
    myAlbum.populate();
});