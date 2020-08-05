import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import {ScrapedataService } from '../../services/scrapedata.service'
import { DomSanitizer } from '@angular/platform-browser';
import { Observable } from 'rxjs';


@Component({
  selector: 'app-resultspage',
  templateUrl: './resultspage.component.html',
  styleUrls: ['./resultspage.component.css']
})
export class ResultspageComponent implements OnInit {
paramTest:string = 'hello'
listingData = placeholder
  constructor(private _router: Router, private route: ActivatedRoute, private ScrapedataService: ScrapedataService, private sanitizer: DomSanitizer) { }

  ngOnInit(): void {
    this.route.queryParams.subscribe(params => {
      this.paramTest = params['searchString'];
      this.ScrapedataService.getEbayData(params['searchString']).subscribe(resEbayLisitings => {
        resEbayLisitings['average_price'] = `£${resEbayLisitings['average_price']}`
        this.listingData = resEbayLisitings
      })
    setTimeout(()=>{
      if(this.listingData.average_price == 'Searching'){
        this.listingData = failedPlaceholder
      }
    }, 4000)
  })
  }

  getSpreadsheet(){
    this.ScrapedataService.createSpreadsheetFile(this.listingData).subscribe(async resFile => {
      console.log(resFile.message);
      window.location.href = `http://localhost:5000/api/send/${resFile.message}`
    })
    
  } 
}

//    placeholder data on async load
const placeholder = {
  average_price: 'Searching',
  image: "https://res.cloudinary.com/dy7eycl8m/image/upload/v1591819721/empty-avatar-png-transparent_mighcw.png",
  name: "Searching",
  results: [
    [
      "Searching",
      '00.00',
      "Searching",
      "#"
    ]
  ]
  } 

  //    Failed to find placeholder
const failedPlaceholder = {
  average_price: 'Not Found',
  image: "https://res.cloudinary.com/dy7eycl8m/image/upload/v1596620667/pngwave_29_de9fmx.png",
  name: "Could not find what you was looking for, please try again",
  results: [
    [
      "Not Found",
      '00.00',
      "Not Found",
      "#"
    ]
  ]
  } 