$(document).ready(function(){
	leftArrows = document.getElementsByClassName("arrowl")
	rightArrows = document.getElementsByClassName("arrowr")
	offsets = []

	for (i=0;i<leftArrows.length;i++) {
		offsets.push($(leftArrows[i]).offset().left);
	}
	for (i=0;i<rightArrows.length;i++) {
		offsets.push($(rightArrows[i]).offset().left);
	}

})