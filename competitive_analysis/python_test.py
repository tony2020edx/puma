

url = "https://www.imdb.com/title/tt0032976/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=0QVVY8DMTSRE0X7AWPAX&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_231"

#remove ? and everthing after it

new_url = url.split("?")[0]

print(new_url)