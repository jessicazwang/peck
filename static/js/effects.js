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
	$('#arrow1r').delay(800).animate({
		opacity:.3
	})

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

	$('img#arrow1r').click(function(){
		$(document).scrollTo($('#box2'),800)
	})
	$('img#arrow2l').click(function(){
		$(document).scrollTo($('#box1'),800)
	})
	$('img#arrow2r').click(function(){
		$(document).scrollTo($('#box3'),800)
	})
	$('img#arrow3l').click(function(){
		$(document).scrollTo($('#box2'),800)
	})
	$('img#arrow3r').click(function(){
		$(document).scrollTo($('#box4'),800)
	})
	$('img#arrow4l').click(function(){
		$(document).scrollTo($('#box3'),800)
	})
	$('img#arrow4r').click(function(){
		$(document).scrollTo($('#box5'),800)
	})
	$('img#arrow5l').click(function(){
		$(document).scrollTo($('#box4'),800)
	})


});


