Number.prototype.toTime = function () {
	d = this;
	var h = Math.floor(d / 3600);
	var m = Math.floor(d % 3600 / 60);
	var s = Math.floor(d % 3600 % 60);
	return ((h > 0 ? h + ":" : "") + (m > 0 ? (h > 0 && m < 10 ? "0" : "") + m + ":" : "0:") + (s < 10 ? "0" : "") + s);
}
function in_array(array, id) {
    for(var i=0;i<array.length;i++) {
        if(array[i] == id) {
            return true;
        }
    }
    return false;
}
$.fn.column = function(callback) {
	var i = $(this).index() + 1;
	if (typeof callback === 'function'){
		$('.puzzel .row .number:nth-child(' + i + ')').each(callback);
	}
}
$.fn.row = function(callback) {
	var i = $(this).parent().index() + 1;
	if (typeof callback === 'function'){
		$('.puzzel .row:nth-child(' + i + ')').each(callback);
	}
}
$.fn.validateRow = function(number) {
	var i = $(this).parent().index() + 1;
	var numbers = [];
	$('.puzzel .row:nth-child(' + i + ') .number').each(function(){
		if ($(this).text() !== ""){
			numbers.push($(this).html());
		}
	});
	if (in_array(numbers, number)){
		console.log("conflict");
		this.row(function(){
			$(this).css('background', "#fff0e8");
		});
	}
}

$(document).ready(function(){
	$('.puzzel .row .number').each(function(){
		if ($(this).text() == "0"){
			$(this).text("");
			$(this).removeClass('fixed');
		}
	});	
	$('.puzzel .row .number').on('focus', function(e){
		$(this).column(function(){
			$(this).css('background', '#f4f8ff');
		});
		$(this).row(function(){
			$(this).css('background', '#f4f8ff');
		})
	});
	$('.puzzel .row .number').on('blur', function(e){
		$(this).column(function(){
			$(this).css('background', 'none');
		});
		$(this).row(function(){
			$(this).css('background', 'none');
		});
	});
	$('.puzzel .row .number').on('keydown', function(e){
		if ($(this).text() !== "" && $(this).hasClass('fixed')){
			if (e.which !== 8){
				e.preventDefault();	
			}
		}else if ($(this).text() !== ""){
			e.preventDefault();	
			$(this).text(String.fromCharCode(e.which));
		}
		$(this).validateRow(parseInt(String.fromCharCode(e.which)));
	});
	
	var count = 0;
	var timer = $.timer(function() {
		$('.timer').html((++count).toTime());
	});
	timer.set({ time : 1000, autostart : true });
});
