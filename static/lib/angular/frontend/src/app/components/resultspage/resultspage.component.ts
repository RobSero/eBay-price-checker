import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import {ScrapedataService} from '../../services/scrapedata.service'


@Component({
  selector: 'app-resultspage',
  templateUrl: './resultspage.component.html',
  styleUrls: ['./resultspage.component.css']
})
export class ResultspageComponent implements OnInit {
paramTest:string = 'hello'
listingData: Object;
  constructor(private route: ActivatedRoute, private ScrapedataService: ScrapedataService) { }

  ngOnInit(): void {
    this.route.queryParams.subscribe(params => {
      this.paramTest = params['searchString'];
      this.ScrapedataService.getEbayData(params['searchString']).subscribe(resEbayLisitings => {
        this.listingData = resEbayLisitings
      })
  })

  }
}
