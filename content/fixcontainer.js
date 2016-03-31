// Created by Paul Gonzalez Becerra

$(window).load(function(args)	{
	resizeContainer(args);
});

$(window).resize(function(args)	{
	resizeContainer(args);
});

function resizeContainer(args)	{
	// Variables
	var	content_container=	$(".content-container");
	
	content_container.height(
		$(args.target).height()-content_container.position().top-1
	);
}

// End of File