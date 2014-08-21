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



});