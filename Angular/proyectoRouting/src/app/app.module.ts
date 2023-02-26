import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomePageComponent } from './pages/home-page/home-page.component';
import { LoginPageComponent } from './pages/login-page/login-page.component';
import { NotFoundComponent } from './pages/not-found/not-found.component';
import { ContactosPageComponent } from './pages/contactos-page/contactos-page.component';
import { ContactosDetailPageComponent } from './pages/contactos-detail-page/contactos-detail-page.component';
import { FormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { RandomContactComponent } from './components/random-contact/random-contact.component';
import { LoginFormComponent } from './components/login-form/login-form.component';
import { RandomContactPageComponent } from './pages/random-contact-page/random-contact-page.component';
import { material } from 'src/material.module';

@NgModule({
  declarations: [
    AppComponent,
    HomePageComponent,
    LoginPageComponent,
    NotFoundComponent,
    ContactosPageComponent,
    ContactosDetailPageComponent,
    RandomContactComponent,
    LoginFormComponent,
    RandomContactPageComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    BrowserAnimationsModule,
    material
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
