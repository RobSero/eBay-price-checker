import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {HomepageComponent} from './components/homepage/homepage.component'
import {ResultspageComponent} from './components/resultspage/resultspage.component'
import {NotfoundComponent} from './components/notfound/notfound.component'


const routes: Routes = [
  {path: '', component: HomepageComponent},
  {path: 'results', component:ResultspageComponent},
  { path: '**', component: NotfoundComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
