var myAlbum = {};

myAlbum.cardArr= [];

myAlbum.toCard = function() {
	console.log(myAlbum.cardArr);
	myAlbum.a = $(this);
	myAlbum.image = $(this).closest('a').find('img').attr('src');
	console.log("sel image", myAlbum.image);

		console.log('test')
		myAlbum.cardArr.push(myAlbum.image);
		myAlbum.cardArr.push("test");
	console.log("cart", myAlbum.cardArr);

	localStorage.setItem("imgData", JSON.stringify(myAlbum.cardArr));
	console.log(myAlbum.cardArr);
	$(".btn.sbold.green.add.card").unbind("click").bind( "click", myAlbum.toCard);
};



//
myAlbum.albumArr=[];
myAlbum.selectToAlbum = function() {
	myAlbum.a = $(this);
	var image = ($(this).closest('a').find('img').attr('src'));
	myAlbum.albumArr.push(image);
	console.log(myAlbum.albumArr);
};



// myAlbum.zoomPicture=function(){
// 	var image = ($(this).closest('a').find('img').attr('src'));
// 	$(".zoom").show();
// 	console.log("here fucking bastards ?");
// 	myAlbum.a = $(this);
// 	myAlbum.a.addClass("zoom");
// 	var d = ($(this).closest('a').find('img').attr('src'));
// 	image.addClass("zoom");
//     };

// myAlbum.orderIt=function(){
// 	myAlbum.b=$(this);
// 	var image = ($(this).closest('a').find('img').attr('src'));
// 	console.log(myAlbum.albumArr);
// 	console.log(myAlbum.cardArr);
// };

myAlbum.start=function(){
	$(".btn.sbold.green.add.card").bind( "click", myAlbum.toCard);
	$(".btn.btn-circle.green.btn-sm.album").unbind("click").bind( "click", myAlbum.selectToAlbum);
	$(".order").unbind("click").bind( "click", myAlbum.orderIt);
	// $(".cbp-item.web-design.graphic.print.motion").unbind("click").bind("click",myAlbum.zoomPicture);
	// $(".zoom").hide();
};


$(document).ready(function() {
    myAlbum.start();
});

