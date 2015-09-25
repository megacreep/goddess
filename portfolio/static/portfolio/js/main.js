jQuery(function($) {

	$(function(){
		$('#main-slider.carousel').carousel({
			interval: 10000,
			pause: false
		});
		$('body').scrollspy({target: '.nav-container'});
	});

	//Ajax contact
	var form = $('.contact-form');
	form.submit(function () {
		$this = $(this);
		$.post($(this).attr('action'), function(data) {
			$this.prev().text(data.message).fadeIn().delay(3000).fadeOut();
		},'json');
		return false;
	});

	//smooth scroll
	$('.navbar-nav > li > a[href^="#"]').click(function(event) {
		event.preventDefault();
		var target = $(this).prop('hash');
		$('html, body').animate({
			scrollTop: $(target).offset().top
		}, 500);
	});

	////scrollspy
	//$('[data-spy="scroll"]').each(function () {
	//	var $spy = $(this).scrollspy('refresh')
	//})

	//PrettyPhoto
	//$("a.preview").prettyPhoto({
	//	social_tools: false
	//});
    //$("a[rel^='prettyPhoto']").prettyPhoto({
     //   social_tools: false
    //});

	//Isotope
	$(window).load(function(){
		$portfolio = $('.portfolio-items');
		$portfolio.isotope({
			itemSelector : 'li',
			layoutMode : 'fitRows'
		});
		$portfolio_selectors = $('.portfolio-filter >li>a');
		$portfolio_selectors.on('click', function(){
			$portfolio_selectors.removeClass('active');
			$(this).addClass('active');
			var selector = $(this).attr('data-filter');
			$portfolio.isotope({ filter: selector });
			return false;
		});
	})

    $(document).ready(function() {
        var sideBar = $(".nav-box");
        var content = $("#project_detail");
        var projects = $("#projects_list");
        if (sideBar) {
            $(".nav-container").height(content.height());
        }
        $(document).scroll(function() {
            $('#position').text($(document).scrollTop() + " " + projects.offset().top);
            if (sideBar.offset().top + sideBar.height() > projects.offset().top) {
                sideBar.css({position: 'absolute', bottom: 0, top: "auto"});
            } else if(sideBar.offset().top - $(document).scrollTop() > 100) {
                sideBar.removeAttr("style");
            }
        });
    });
});