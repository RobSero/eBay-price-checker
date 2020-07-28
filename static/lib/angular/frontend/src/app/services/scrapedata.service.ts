import { Injectable } from '@angular/core';
import {Observable} from 'rxjs'
import {HttpClient, HttpHeaders, HttpResponse} from '@angular/common/http'

let header = new HttpHeaders();
header.set('Access-Control-Allow-Origin', '*');
header.set('responseType', 'ResponseContentType.Blob');

@Injectable({
  providedIn: 'root'
})
export class ScrapedataService {
apiURL:string = 'http://localhost:5000/api/search/'


  constructor(private http:HttpClient) { }


// get data from api, requires search string argument
getEbayData(searchParam: string): Observable<any>{
  return this.http.get<any>(`${this.apiURL}${searchParam}`)
}

getSpreadsheetFile(listingInfo:Object): Observable<HttpResponse<Blob>>{
  console.log('getting file now');
  return this.http.post<any>('http://localhost:5000/api/send',listingInfo , {headers: header} )
}

}
