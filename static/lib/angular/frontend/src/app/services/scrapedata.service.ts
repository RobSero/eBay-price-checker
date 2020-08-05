import { Injectable } from '@angular/core';
import {Observable} from 'rxjs'
import {HttpClient, HttpHeaders, HttpResponse} from '@angular/common/http'

let header = new HttpHeaders();
// header.set('Access-Control-Allow-Origin', '*');
header.set('responseType', 'ResponseContentType.Blob');
header.set('cheese', 'tastes good');

@Injectable({
  providedIn: 'root'
})
export class ScrapedataService {
apiURL:string = 'https://ebuddyscraper.herokuapp.com/api/search/'


  constructor(private http:HttpClient) { }


// get data from api, requires search string argument
getEbayData(searchParam: string): Observable<any>{
  return this.http.get<any>(`api/search/${searchParam}`)
}

createSpreadsheetFile(listingInfo:Object): Observable<any>{
  console.log('getting file now');
  return this.http.post<any>('api/send',listingInfo)
}

}
