#define EEFC_FKEY 0x5A
#define EEFC_FMR_SCOD   (0x1ul << 16)
#define IFLASH0_ADDR  0x00080000                               // Flash memory begins at 0x00080000
#define IFLASH1_ADDR ( IFLASH0_ADDR + IFLASH_SIZE / 2 )        // IFLASH1_ADDR  = 0x000C0000


__attribute__ ((section (".ramfunc")))
void ReadUniqueID( uint32_t * latch_buffer )
{
    char __FWS;

                                                                  // Set bit 16 of EEFC_FMR : See chap. 49.1.1.2 page 1442
    EFC0->EEFC_FMR |= EEFC_FMR_SCOD;                              // Sequential code optimization disable

  __FWS = (EFC0->EEFC_FMR & EEFC_FMR_FWS_Msk)>>EEFC_FMR_FWS_Pos ; // Save FWS value
    EFC0->EEFC_FMR &=~ EEFC_FMR_FWS_Msk;
    EFC0->EEFC_FMR |= EEFC_FMR_FWS(6);                            // 6+1 wait states for read and write operations


    EFC0->EEFC_FMR &=~EEFC_FMR_FAM;                               // 128-bit access in read Mode only, to enhance access speed.

    while(!(EFC0->EEFC_FSR & EEFC_FSR_FRDY));                     // Send the  STUI command if FRDY bit is high to begin reading in flash
    EFC0->EEFC_FCR = EEFC_FCR_FKEY(EEFC_FKEY) | EFC_FCMD_STUI ;
                                                                  //Wait till FRDY falls down
    while(EFC0->EEFC_FSR & EEFC_FSR_FRDY);
                                                                  // The Unique Identifier is located in the first 128 bits of
                                                                  // the Flash bank 0 in between 0x080000 and 0x08000C (and of the Flash bank 1 in between 0X0C0000 and 0x0C000C ??)
    memcpy(latch_buffer, (void*)IFLASH0_ADDR, 16);                // Read first 128 bits ( 16 first bytes) in one shot beginning at address IFLASHIndex_ADDR

                                                                  // Send the SPUI command to stop reading in flash
    EFC0->EEFC_FCR = EEFC_FCR_FKEY(EEFC_FKEY) | EFC_FCMD_SPUI ;
                                                                  // Wait till FRDY rises up
    while(!(EFC0->EEFC_FSR & EEFC_FSR_FRDY));

                                                                  // Clear bit 16 of EEFC_FMR : See chap. 49.1.1.2 page 1442
    EFC0->EEFC_FMR &= ~EEFC_FMR_SCOD;                             // Sequential code optimization enable

    EFC0->EEFC_FMR &=~ EEFC_FMR_FWS_Msk;                          // Restore FWS value
    EFC0->EEFC_FMR |= EEFC_FMR_FWS(__FWS);

}

void setup ()
{
Serial.begin (250000) ;
                /***********   Read Unique ID  ***************************/
    uint32_t latch_buffer[4];
    ReadUniqueID( latch_buffer ) ;
    Serial.println("Reading of the 128 bits unique identifier :"); Serial.print(" ID = " );

    for (byte b = 0 ; b < 4 ; b++)
     {
      Serial.print((uint32_t)latch_buffer[b], HEX) ;Serial.print((uint32_t)(latch_buffer[b]>>32), HEX);
     }


}

void loop() {}
