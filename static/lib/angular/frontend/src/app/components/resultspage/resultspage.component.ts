import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
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
  constructor(private route: ActivatedRoute, private ScrapedataService: ScrapedataService, private sanitizer: DomSanitizer) { }

  ngOnInit(): void {
    this.route.queryParams.subscribe(params => {
      this.paramTest = params['searchString'];
      this.ScrapedataService.getEbayData(params['searchString']).subscribe(resEbayLisitings => {
        resEbayLisitings['average_price'] = `£${resEbayLisitings['average_price']}`
        this.listingData = resEbayLisitings
      })
  })
  }

  getSpreadsheet(){
    this.ScrapedataService.getSpreadsheetFile(this.listingData).subscribe(resFile => {
      console.log('got file');
      
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