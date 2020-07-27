import { Component, OnInit, Output, EventEmitter, Input } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.css']
})
export class HomepageComponent implements OnInit {
userInput:string
@Output() searchProduct: EventEmitter<any> = new EventEmitter()

  constructor(private _router: Router) {}
  ngOnInit(): void {
  }

  printInput(){
    console.log(this.userInput);
  }

submitForm(){
  this._router.navigate(['/results'], {
    queryParams: {
      searchString: this.userInput
    },
    queryParamsHandling: 'merge',
    // preserve the existing query params in the route
    skipLocationChange: true
    // do not trigger navigation
  })
}
}
