#Pass the file name as a argument
$listOfservers=$args[0]

gc $listOfservers | foreach {
    $srv = $_
    $pingtest = Test-Connection -ComputerName $srv -Quiet -Count 1 -ErrorAction SilentlyContinue
    if($pingtest) {
         $pingOut =  "Online"
      }
     else {
   
       $pingOut =  "Offline"
     }

    try { 
        $abc = Resolve-DnsName -Name $srv -ErrorAction Stop
        $ip = $abc.IPAddress
    }
    catch {
         $ip = "---"
    }
    

    "$srv , $pingOut, $ip" | Out-File ./out.csv -Encoding utf8 -Append
}
