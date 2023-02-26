import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RandomContactComponent } from './components/random-contact/random-contact.component';
import { AuthGuard } from './guards/auth.guard';
import { ContactosDetailPageComponent } from './pages/contactos-detail-page/contactos-detail-page.component';
import { ContactosPageComponent } from './pages/contactos-page/contactos-page.component';
import { HomePageComponent } from './pages/home-page/home-page.component';
import { LoginPageComponent } from './pages/login-page/login-page.component';
import { NotFoundComponent } from './pages/not-found/not-found.component';
import { RandomContactPageComponent } from './pages/random-contact-page/random-contact-page.component';

const routes: Routes = [
  {
    path: '',
    pathMatch: 'full',
    redirectTo: 'home'
  },

  {
    path:'login',
    component: LoginPageComponent
  },

  {
    path: 'home',
    component: HomePageComponent,
    children: [
      {
        path: 'hijo',
        component: HomePageComponent
      }
    ],
    canActivate: [AuthGuard]
  },

  {
    path: 'contacts',
    component: ContactosPageComponent,
    canActivate: [ AuthGuard ]
  },

  {
    path: 'contacts/:id',
    component: ContactosDetailPageComponent,
    canActivate: [ AuthGuard ]
  },
  
  {
    path: 'random',
    component: RandomContactPageComponent,
    canActivate: [ AuthGuard ]
  },

  {
    path: '**',
    component: NotFoundComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
