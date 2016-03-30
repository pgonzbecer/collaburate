// Created by Paul Gonzalez Becerra

package main;

import (
	"net/http"
	"html/template"
);

// Variables
var	templates=	template.Must(template.ParseFiles(
	"templates/navbar.html",
	"templates/proj_title.html",
	"templates/proj_sidebar.html",
	"templates/proj_content.html",
	"templates/profile_title.html",
	"templates/profile_content.html",
	"templates/profile_sidebar.html",
));

// Start of the application
func main()	{
	http.HandleFunc("/proj/", projHandler);
	http.ListenAndServe("127.0.0.1:8080", nil);
}

// Handles the web page request
func projHandler(w http.ResponseWriter, r *http.Request)	{
	renderProjectPage(w);
}

// Renders the given template
func renderTemplate(w http.ResponseWriter, pmTemplate string, obj interface{})	{
	// Variables
	err:=	templates.ExecuteTemplate(w, pmTemplate+".html", obj);
	
	if(err!= nil)	{
		http.Error(w, err.Error(), http.StatusInternalServerError);
	}
}

func renderProfilePage(w http.ResponseWriter)	{
	renderTemplate(w, "templates/navbar", nil);
}

// Renders the project's page
func renderProjectPage(w http.ResponseWriter)	{
	renderTemplate(w, "navbar", nil);
	renderTemplate(w, "proj_title", nil);
	renderTemplate(w, "proj_sidebar", nil);
	renderTemplate(w, "proj_content", nil);
}

// End of File