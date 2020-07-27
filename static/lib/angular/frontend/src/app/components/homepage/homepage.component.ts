import { Component, OnInit, Output, EventEmitter, Input } from '@angular/core';

@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.css']
})
export class HomepageComponent implements OnInit {
userInput:string
@Output() searchProduct: EventEmitter<any> = new EventEmitter()

  constructor() { }
  ngOnInit(): void {
  }

  printInput(){
    console.log(this.userInput);
  }

submitForm(){
  this.searchProduct.emit(this.userInput)
}
}
