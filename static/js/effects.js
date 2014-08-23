$(document).ready(function(){
	$("#crest").animate({
		opacity:1,
		marginTop:"+=20"
	},1500);
	$("#title-h1").delay(600).animate({
			opacity:1,
			marginLeft:"+=25"
	},1500);
	$("#title-h2").delay(600).animate({
			opacity:1,
			marginRight:"+=20"
	},1500);

	$(function() {
		$('div#brother').makeCaption({
		animation: 'fadeIn', // move, slide, fadeIn, scaleIn, rotate, or push
		position: 'Below' // Below or Above
		});
	});

	$('a#brother').click(function(){
		var brother;
		brother = $(this).attr("data-componentID");
		$.get('/getBrother', {bro: brother}, function(data){
			info = JSON.parse(data)
			$('.modal-content .name').html(info['name'])
			$('.modal-content .initials').html(info['initials'])
			$('.modal-content .nickname').html(info['nickname'])
			$('.modal-content .quote').html(info['quote'])
			$('.modal-content .hometown').html(info['hometown'])
			$('.modal-content .major').html(info['major'])
			$('.modal-content .activities').html(info['activities'])
			$('.modal-content .blurb').html(info['blurb'])
			$('.modal-content .photo').html("<img src='"+info['photo']+"'>")

		})
	})





});